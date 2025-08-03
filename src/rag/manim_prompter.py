from src.llm.deepseek import chat_completion
from src.rag.types import input_prompt


def manim_prompter(prompt: str):
    prompt_template = f"""
    You are an expert Manim animation engineer.

    Your job is to take a user request and generate a complete Python script using Manim (Community Edition, manimce) 
    that can be run directly to render the animation.


    🔒 Rules:
        Generate a Manim script that does the following:
        Shows x and y coordinate axes
        Marks key points at π/2, π, 3π/2, and 2π on the x-axis
        Draws a sine wave gradually from 0 to 2π
        Animates a red dot tracking the wave as it's drawn
        Marks the end of the wave at (2π, 0) with a green dot and label
        Return only a JSON object with the Manim Python code under the key "manim"
        Do not include markdown, explanations, or any extra text.
        The output must be like:

    ```json
    {{
      "manim": "```python\\n# your manim code here\\n```"
    }}

    here is the user prompt = {prompt}
    """

    response = chat_completion(prompt_template)
    return response

manim_prompter("visualize sine wave")