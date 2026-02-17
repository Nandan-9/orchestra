


def build_manim_prompt(plan):

    concept = plan["concept"]
    A = plan["example"]["A"]
    B = plan["example"]["B"]
    visual_plan = plan["visual_plan"]

    prompt_lines = []

    prompt_lines.append("You are an Expert Manim Animation Engineer.")
    prompt_lines.append("Generate executable Manim CE Python code.")
    prompt_lines.append("Use ONLY valid Manim syntax.")
    prompt_lines.append("")
    prompt_lines.append(f"Concept: {concept}")
    prompt_lines.append(f"Matrix A: {A}")
    prompt_lines.append(f"Matrix B: {B}")
    prompt_lines.append("")
    prompt_lines.append("Follow this exact animation plan:")

    for step in visual_plan:
        prompt_lines.append(
            f"Step {step['step']}: "
            f"{step['action']} with parameters {step['parameters']}"
        )

    prompt_lines.append("")
    prompt_lines.append("Only output valid Python Manim code. No markdown.")

    return "\n".join(prompt_lines)


def video_generate(plan):

    mainm_prompt = build_manim_prompt(plan)
    return mainm_prompt


