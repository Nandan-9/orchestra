


def build_manim_prompt(plan):


    prompt_lines = []

    prompt_lines.append("You are an Expert Manim Animation Engineer.")
    prompt_lines.append("Generate executable Manim CE Python code.")
    prompt_lines.append("Use ONLY valid Manim syntax.")
    prompt_lines.append("")
    prompt_lines.append(f"Concept: {plan}")

    prompt_lines.append("")
    prompt_lines.append("Follow this exact animation plan:")

    prompt_lines.append("In the concept there is Visual_plan it is the plan on how to animate the video")
    prompt_lines.append("Only output valid Python Manim code. No markdown.")

    return "\n".join(prompt_lines)


def video_generate(plan):

    mainm_prompt = build_manim_prompt(plan)
    return mainm_prompt


