import json
import os
from datetime import datetime

def load_templates():
    with open("prompts/prompt_templates.json", "r") as f:
        return json.load(f)

def save_output(task, prompt, output):
    log = {
        "timestamp": datetime.now().isoformat(),
        "task": task,
        "prompt": prompt,
        "output": output
    }
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/saved_prompts.json", "a") as f:
        f.write(json.dumps(log) + "\n")