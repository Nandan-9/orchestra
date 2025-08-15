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

    # Ensure the output folder exists locally
    output_dir = os.path.join(folder_path, "output")
    os.makedirs(output_dir, exist_ok=True)

    # Make the source file readable
    os.chmod(abs_path, 0o644)

    # Optional: run Docker as current user
    user_id = os.getuid()

    subprocess.run([
        "docker", "run", "--rm",
        "-u", str(user_id),
        "-v", f"{folder_path}:/app:Z",  # Mount working directory
        "manimcommunity/manim:stable",
        "manim", "-ql", f"/app/{file_name}",
        scene_name,
        "--media_dir", f"/app/output/{scene_name}",  # Folder named after scene
        "-o", scene_name  # File name = scene name
    ])

    video_path = os.path.join(
        folder_path,
        "output", scene_name, "videos", scene_name, "480p15", f"{scene_name}.mp4"
    )

    print(f"Video saved at: {video_path}")