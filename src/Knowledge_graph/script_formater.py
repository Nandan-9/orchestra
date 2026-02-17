import re
from llm import chat_completion

def convert_math_to_speech(text: str) -> str:
    # Replace summation
    text = re.sub(
        r"\\sum_{k=1}^{n}",
        "the summation from k equals 1 to n",
        text
    )

    # Replace subscripts like A_{ik}
    text = re.sub(
        r"A_{ik}",
        "A i k",
        text
    )

    text = re.sub(
        r"B_{kj}",
        "B k j",
        text
    )

    text = re.sub(
        r"\(AB\)_{ij}",
        "A B sub i j",
        text
    )

    # Remove LaTeX brackets
    text = re.sub(r"\\[a-zA-Z]+", "", text)
    text = re.sub(r"[{}]", "", text)

    return text


def format_for_speech(text: str) -> str:
    text = convert_math_to_speech(text)

    # Remove markdown
    text = text.replace("**", "")
    text = text.replace("*", "")

    # Add smoother transitions
    text = text.replace("In other words,", "To understand this more clearly,")

    return text



def add_narration_pauses(text: str) -> str:
    # Add pauses after full stops
    text = text.replace(". ", ". <break time='700ms'/> ")

    # Add slight pause before examples
    text = text.replace("Example", "<break time='1000ms'/> Now let's look at an example.")

    return text


def create_naration(text: str):

    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input text for narration is empty")

    prompt = f"""
You are a professional academic voice-over script writer for animated mathematics videos.

Rewrite the following explanation as a smooth spoken narration.

Requirements:

- Remove all symbols, LaTeX, equations, markdown, and formatting.
- Convert mathematical notation into spoken language.
- Explain formulas step by step in words.
- Maintain logical teaching order.
- Use clear and natural sentences.
- Add smooth transitions between ideas.
- Do not mention section titles.
- Do not use bullet points.
- Output plain narration text only.

Text to convert:

{text}
"""
    messages=[
            {"role": "system", "content": "You are an expert educational narrator."},
            {"role": "user", "content": prompt}
        ]
    response = chat_completion(messages)
    return response



def build_narration(plan):

    concept = plan["concept"]
    definition = plan["definition"]
    A = plan["example"]["A"]
    B = plan["example"]["B"]

    script_lines = []

    script_lines.append(f"Let's understand {concept}.")
    script_lines.append(definition)
    script_lines.append(f"Consider matrix A as {A} and matrix B as {B}.")
    script_lines.append("Now we compute each element step by step.")

    for step in plan["visual_plan"]:

        action = step["action"]
        params = step["parameters"]

        if action == "check_dimension_match":
            script_lines.append(
                f"We check that the number of columns in A is {params['columns_A']} "
                f"and rows in B is {params['rows_B']}. Multiplication is possible."
            )

        elif action == "show_dot_product_calculation":
            script_lines.append(
                f"Now we compute: {params['calculation']}."
            )

        elif action == "display_result_matrix":
            script_lines.append(
                f"The final result matrix is {params['result_matrix']}."
            )

    script_lines.append("These are the prerequisites you should know before this topic.")
    for prereq in plan["prerequisites"]:
        script_lines.append(prereq)

    return " ".join(script_lines)

def generate_voice_over(explanation_text: str):
    narration = build_narration(explanation_text)
    speech = create_naration(narration)

    return speech