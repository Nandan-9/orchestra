from src.llm.deepseek import chat_completion
from src.rag.types import input_prompt


def manim_prompter(prompt: str):
    prompt_template = f"""
    You must output ONLY a valid JSON object in exactly this format:

    {{
      "manim": "# full runnable Python code using ManimCE here"
    }}

    Do NOT include:
    - Markdown code fences
    - Comments or explanations
    - Extra keys
    - Any text before or after the JSON

    Your role:
    You are an expert Manim animation engineer.
    Write a complete Python script using Manim (Community Edition) that can be run directly to render the animation.

    User request: {prompt}

    Final rule: Return ONLY the JSON object described at the start.
    """

    response = chat_completion(prompt_template)
    return response

