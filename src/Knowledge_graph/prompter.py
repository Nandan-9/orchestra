from graph import retrieve_subgraph
from llm import chat_completion
from script_formater import generate_voice_over
from audio_generator import text_to_speech
from video_generator import video_generate
# from src.rag.manim_prompter import manim_prompter

def ask_kg_rag(question):
    # 1. Retrieve Context
# 1. Get Context AND Prerequisites
    context_text, prereq_list = retrieve_subgraph(question)

    # print(context_text)
    
    if not context_text:
        return "No information found."

    # Format the prereqs as a bullet list string
    prereq_str = "\n- ".join(prereq_list) if prereq_list else "None identified in graph."

    system_prompt = """
You are an Adaptive Math Tutor AND Visual Instruction Planner.

You must return STRICTLY valid JSON in the following schema:

{
  "concept": "...",
  "definition": "...",
  "example": {
      "A": [[...]],
      "B": [[...]]
  },
  "visual_plan": [
      {
        "step": 1,
        "action": "...",
        "parameters": { ... }
      }
  ],
  "prerequisites": ["...", "..."]
}

--------------------------------------------------
VISUAL PLAN RULES (VERY IMPORTANT)

You are not describing math.
You are describing WHAT SHOULD APPEAR ON SCREEN.

Each visual_plan step must describe:

- What object appears
- What gets highlighted
- What gets computed
- What text appears

You MUST choose actions ONLY from this allowed list:

Allowed actions:

1. "display_matrices"
   Parameters:
   {
     "show_A": true/false,
     "show_B": true/false
   }

2. "check_dimension_match"
   Parameters:
   {
     "columns_A": integer,
     "rows_B": integer
   }

3. "highlight_row_and_column"
   Parameters:
   {
     "row_index": integer,
     "column_index": integer
   }

4. "show_dot_product_calculation"
   Parameters:
   {
     "row_index": integer,
     "column_index": integer,
     "calculation": "string showing exact math expression"
   }

5. "display_result_entry"
   Parameters:
   {
     "row_index": integer,
     "column_index": integer,
     "value": number
   }

6. "display_result_matrix"
   Parameters:
   {
     "result_matrix": [[...]]
   }

--------------------------------------------------

STRICT REQUIREMENTS:

- Each step must correspond to a visible animation.
- Do NOT describe abstract reasoning.
- Do NOT write explanations inside visual_plan.
- Only include actions that can be animated.
- Output ONLY JSON.

Use ONLY information from the Context Graph.
"""
    
    user_prompt = f"""
    Context Graph:
    {context_text}
    
    Prerequisites List (Detected from Graph):
    - {prereq_str}
    
    User Question: {question}
    """
    
    # 3. Call LLM
    messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    response = chat_completion(messages)
    
    
    return response






def main_prompter(chat):
    # question = "What is matrix Multiplication? Can you give me an example"
    # question = question
    answer = ask_kg_rag(chat)
    speech = generate_voice_over(answer)
    manim_script = video_generate(answer)
    print("Question : ",chat)
    print(f"\nAI Answer:\n{answer}\n" + "-"*40)
    print("nations speech")
    print(speech)
    print(text_to_speech(speech))
    return manim_script



 
question = "What is matrix Multiplication? Can you give me an example"

answer = ask_kg_rag(question)
speech = generate_voice_over(answer)
voice_path = text_to_speech(speech)
manim_script = video_generate(answer)
print("Question : ",question)
print(f"\nAI Answer:\n{answer}\n" + "-"*40)
print("nations speech")
print(speech)
print()



