from evaluator import compare_outputs
from utils import load_templates, save_output
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
print("Current working directory:", os.getcwd())
from groq import Groq

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("Missing GROQ_API_KEY. Please set it in your .env file.")

client = Groq(api_key=groq_api_key)


def get_llm_response(prompt, model="llama-3.3-70b-versatile", temperature=0.7):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content

def main():
    task = input("Describe your task:\n> ")
    templates = load_templates()

    print("\nGenerating prompt variants...\n")
    variants = [template.replace("{{task}}", task) for template in templates]

    for i, prompt in enumerate(variants):
        print(f"--- Prompt Variant {i+1} ---\n{prompt}\n")
        output = get_llm_response(prompt)
        print(f"Output:\n{output}\n")
        save_output(task, prompt, output)

    compare_outputs()

if __name__ == "__main__":
    main()