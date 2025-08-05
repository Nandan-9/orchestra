import os
import re
import subprocess


def save_code(code: str, scene_id: str):
    os.makedirs("manim_code", exist_ok=True)
    file_path = f"manim_code/{scene_id}.py"
    with open(file_path, "w") as f:
        f.write(code)

    # Extract class name from code
    match = re.search(r"class\s+(\w+)\(Scene\):", code)
    if not match:
        raise ValueError("No Scene class found in the code.")

    scene_class = match.group(1)
    return file_path, scene_class


def render_manim_scene(file_path: str, scene_name: str, output_name: str):
    abs_path = os.path.abspath(file_path)
    container_path = "/app/" + os.path.basename(file_path)

    subprocess.run([
        "docker", "run", "--rm",
        "-v", f"{os.path.dirname(abs_path)}:/app",
        "manimcommunity/manim:stable",
        "manim", "-pql", container_path, scene_name, "-o", output_name
    ])
