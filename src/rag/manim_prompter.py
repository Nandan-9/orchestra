from src.rag.lang_chain import get_rag_chain
from src.llm.deepseek import chat_completion
from src.rag.types import input_prompt




retrieval_chain = get_rag_chain()

def manim_prompter(prompt: str):
    prompt_template = f"""
You are an Expert Manim Community Edition (ManimCE) Animation Engineer.

You MUST strictly follow these rules:

OUTPUT FORMAT:
Return ONLY a valid JSON object in EXACTLY this format:

{{
  "manim": "full runnable Python code using ManimCE"
}}

STRICT CONSTRAINTS:
- No markdown
- No comments
- No explanations
- No extra keys
- No text before or after JSON
- Code must run directly with ManimCE
- Import using: from manim import *
- Define exactly ONE Scene class
- Do NOT invent APIs
- Use only valid ManimCE classes and methods
- Ensure syntactically valid Python
- Ensure no undefined variables
- Ensure animations use valid methods like Create, FadeIn, Write, Transform, etc.
- Include wait() where appropriate

GROUNDING RULE:
Use ONLY APIs and syntax consistent with official ManimCE documentation.

User Request:
{prompt}

Final Rule:
Return ONLY the JSON object.
"""

    response = retrieval_chain.invoke({
        "input": prompt_template
    })["answer"]

    return response
