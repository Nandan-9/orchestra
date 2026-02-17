import json
import networkx as nx
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI # For OpenRouter


JSON_FILE = "/home/das/pro/orchestra/src/Knowledge_graph/outputs/knowledge_triples.json"


print("Loading Knowledge Graph...")
with open(JSON_FILE, "r") as f:
    triples = json.load(f)

G = nx.DiGraph()
for item in triples:

    G.add_edge(item['head'], item['tail'], relation=item['relation'])

print("Embedding Graph Nodes (this may take a moment)...")
embedder = SentenceTransformer('all-MiniLM-L6-v2') 

all_nodes = list(G.nodes())
node_embeddings = embedder.encode(all_nodes)


def get_prerequisites(concept, depth=2):
    prereqs = set()
    queue = [(concept, 0)]

    while queue:
        node, d = queue.pop(0)
        if d >= depth:
            continue

        for pred in G.predecessors(node):
            if G[pred][node]['relation'] == 'REQUIRES':
                prereqs.add(pred)
                queue.append((pred, d + 1))

    return prereqs


# 3. RETRIEVAL FUNCTION (The "Graph" part of RAG)
def retrieve_subgraph(query, top_k=3):
    # 1. Vector Search to find the main topic node
    query_emb = embedder.encode([query])
    similarities = cosine_similarity(query_emb, node_embeddings)[0]
    top_indices = np.argsort(similarities)[-1:][::-1] # Get top 1 most relevant node
    main_topic_node = all_nodes[top_indices[0]]
    
    context_lines = []
    prereq_lines = []
    
    # 2. Standard Context Retrieval (Neighbors)
    if main_topic_node in G:
        for neighbor in G.neighbors(main_topic_node):
            relation = G[main_topic_node][neighbor]['relation']
            source_id = G[main_topic_node][neighbor].get('source', 'General')
            
            # Formatting the triple
            triple_str = f"[Source: {source_id}] {main_topic_node} --[{relation}]--> {neighbor}"
            context_lines.append(triple_str)
            
            # 3. PREREQUISITE CHECK (The Magic Step)
            # We look for specific relation types that imply dependency
            if relation in ["REQUIRES", "DEPENDS_ON", "BASED_ON", "EXTENDS"]:
                # This neighbor is a prerequisite!
                prereq_lines.append(neighbor)

        # 4. Backward check: Did something else say it is a prerequisite for this?
        # e.g., (Addition, PREREQUISITE_FOR, Multiplication)
        for predecessor in G.predecessors(main_topic_node):
            relation = G[predecessor][main_topic_node]['relation']
            if relation in ["PREREQUISITE_FOR", "LEADS_TO"]:
                prereq_lines.append(predecessor)

    return "\n".join(context_lines), list(set(prereq_lines))