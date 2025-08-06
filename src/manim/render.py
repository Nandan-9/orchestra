import os
import re
import subprocess
import getpass


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
    folder_path = os.path.dirname(abs_path)
    file_name = os.path.basename(file_path)

    os.chmod(abs_path, 0o644)

    # Optional: add current user id for Docker
    user_id = os.getuid()

    subprocess.run([
        "docker", "run", "--rm",
        "-u", str(user_id),  # Run Docker with your user ID
        "-v", f"{folder_path}:/app:Z",
        "manimcommunity/manim:stable",
        "manim", "-pql", f"/app/{file_name}", scene_name, "-o", output_name
    ])
