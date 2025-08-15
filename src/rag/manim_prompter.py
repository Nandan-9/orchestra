from src.llm.deepseek import chat_completion
from src.rag.types import input_prompt


def manim_prompter(prompt: str):
    prompt_template = f"""
    You must output ONLY a valid JSON object in exactly this format:

    {{{{  
      "manim": "# full runnable Python code using ManimCE here"
    }}}}

    Do NOT include:
    - Markdown code fences
    - Comments or explanations
    - Extra keys
    - Any text before or after the JSON

    Your role:
    You are an expert Manim animation engineer.
    Write a complete Python script using Manim (Community Edition) that can be run directly to render the animation.

    Animation requirements:
    1. Show x and y coordinate axes.
    2. Mark key points at π/2, π, 3π/2, and 2π on the x-axis.
    3. Draw a sine wave gradually from 0 to 2π.
    4. Animate a red dot tracking the wave as it’s drawn.
    5. Mark the end of the wave at (2π, 0) with a green dot and label.

    User request: {prompt}

    Final rule: Return ONLY the JSON object described at the start.
    """

    response = chat_completion(prompt_template)
    return response

