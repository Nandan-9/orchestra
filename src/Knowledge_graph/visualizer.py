import json
import networkx as nx
from pyvis.network import Network
import os

# 1. Load the data
# If you have the list in memory, use it. Otherwise load from file:
try:
    with open("outputs/knowledge_triples.json", "r") as f:
        triples = json.load(f)
except FileNotFoundError:
    print("File not found. Please ensure 'outputs/knowledge_triples.json' exists.")
    # Use the sample data you provided just to demonstrate
    triples = [
        {"head": "Matrices", "relation": "IS_A", "tail": "Mathematical Tool", "source": "3.1"},
        {"head": "Matrices", "relation": "USED_IN", "tail": "Cryptography", "source": "3.1"},
        {"head": "Column Matrix", "relation": "DEFINED_AS", "tail": "Matrix with 1 column", "source": "3.3"}
    ]

# 2. Initialize the NetworkX Graph
G = nx.DiGraph()

# 3. Add Nodes and Edges
for item in triples:
    # We add the 'title' attribute so when you hover over a node/edge in HTML, 
    # it shows the source section!
    
    # Add Nodes
    G.add_node(item['head'], title=item.get('source', ''), color='#97c2fc')
    G.add_node(item['tail'], title=item.get('source', ''), color='#ffffbf') # Yellow for objects
    
    # Add Edge
    G.add_edge(
        item['head'], 
        item['tail'], 
        label=item['relation'], 
        title=f"Source: {item.get('source', 'Unknown')}"
    )

print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# 4. Configure PyVis (The Interactive View)
net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=False)

# Force the layout to be more "Physics" based so nodes float apart nicely
net.force_atlas_2based()

# Convert from NetworkX to PyVis
net.from_nx(G)

# 5. Save and Open
output_file = "ncert_matrices_graph.html"
net.show(output_file, notebook=False)
print(f"Visualization saved to '{output_file}'. Open this file in your browser!")