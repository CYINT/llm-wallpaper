import argparse
import os
import platform
import subprocess
import sys
import time
from typing import List

try:
    import openai
except ImportError:
    print("openai package not found. Install with `pip install openai`.")
    sys.exit(1)

try:
    import pyautogui
except ImportError:
    pyautogui = None


def set_wallpaper(path: str):
    system = platform.system()
    if system == "Windows":
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
    elif system == "Darwin":
        script = f'tell application "System Events" to set picture of every desktop to POSIX file "{path}"'
        subprocess.run(["osascript", "-e", script], check=True)
    else:
        print(f"Setting wallpaper not implemented for {system}.")


def capture_screenshot() -> str:
    if not pyautogui:
        raise RuntimeError("pyautogui is required for screenshot input")
    screenshot = pyautogui.screenshot()
    path = os.path.join(os.getcwd(), "screenshot.png")
    screenshot.save(path)
    return path


def fetch_x_posts() -> str:
    # Placeholder for fetching posts from X (Twitter)
    # In a real implementation, use the X API with the user's credentials
    return ""


def generate_prompt(base_prompt: str, inputs: List[str]) -> str:
    details = []
    for item in inputs:
        if item == "screenshot":
            path = capture_screenshot()
            details.append(f"Screenshot saved at {path}")
        elif item == "xposts":
            posts = fetch_x_posts()
            details.append(f"Recent X posts: {posts}")
    if details:
        base_prompt += "\n" + "\n".join(details)
    return base_prompt


def generate_wallpaper(llm_key: str, prompt: str) -> str:
    openai.api_key = llm_key
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    url = response['data'][0]['url']
    import requests
    img_data = requests.get(url).content
    path = os.path.join(os.getcwd(), "wallpaper.png")
    with open(path, 'wb') as f:
        f.write(img_data)
    return path


def main():
    parser = argparse.ArgumentParser(description="Generate wallpaper with LLM")
    parser.add_argument("--llm-key", help="API key for the LLM", default=os.getenv("OPENAI_API_KEY"))
    parser.add_argument("--prompt", help="Prompt for the LLM", default="Create a beautiful wallpaper")
    parser.add_argument("--interval", type=int, help="Interval in minutes for changing wallpaper")
    parser.add_argument("--inputs", default="", help="Comma separated inputs like screenshot,xposts")
    args = parser.parse_args()

    if not args.llm_key:
        print("Missing LLM API key. Provide with --llm-key or OPENAI_API_KEY.")
        return

    input_list = [i.strip() for i in args.inputs.split(',') if i.strip()]

    def run_cycle():
        final_prompt = generate_prompt(args.prompt, input_list)
        img_path = generate_wallpaper(args.llm_key, final_prompt)
        set_wallpaper(img_path)
        print(f"Wallpaper updated with prompt: {final_prompt}")

    if args.interval:
        while True:
            run_cycle()
            time.sleep(args.interval * 60)
    else:
        run_cycle()


if __name__ == "__main__":
    main()
