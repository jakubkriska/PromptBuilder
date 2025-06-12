
# 🧠 PromptBuilder

PromptBuilder helps you experiment with and refine prompts for Large Language Models (LLMs). Describe your task, and the app generates multiple prompt variants with different tones and structures—perfect for testing and improving prompt quality.

You can run it via CLI or a Streamlit web interface, using Groq-hosted models like `llama-3.3-70b-versatile`.

---

## 📁 Project Structure

<pre>
prompt-builder/
├── main.py                     # Entry point to run the CLI
├── prompts/
│   └── prompt_templates.json   # Templates for generating prompt variants
├── outputs/
│   ├── saved_prompts.json         # Prompt/output log (Git-ignored)
│   └── saved_prompts.example.json # Sample structure for reference
├── evaluator.py                # Handles user evaluation of outputs
├── utils.py                    # Helper functions: loading templates, saving logs
└── README.md                   # Project overview and instructions
</pre>

---

## 🧪 Features

- Generate multiple LLM prompt variants from a single task
- Automatically call OpenAI or Groq APIs
- View and compare output quality
- Save and log prompts for later analysis
- CLI-based and easy to extend

---

## 🚀 Getting Started

```bash
pip install -r requirements.txt
# If using the Streamlit UI:
pip install streamlit

# Create a .env file and add your Groq API key:
echo "GROQ_API_KEY=your-groq-api-key-here" > .env

python main.py
```

Note: The file `outputs/saved_prompts.json` is automatically created to log generated prompts and outputs. It is ignored by Git. A sample file `saved_prompts.example.json` is included in the same folder to show the expected format.

---

## 🖥️ Using the Streamlit Interface

To launch the app in your browser:

```bash
streamlit run streamlit_app.py
```

In the UI, you can:
- Enter your task
- Choose a model (Groq-supported)
- Generate and compare prompt variants
- Copy or save the best results

---

## 🧪 Example Prompt Variants

**Task**:  
You are a personal assistant. Write in the style of the person who uses you.

**Prompt Variants**:
- *Direct*:  
  “Act as my assistant. Use my tone in everything you write. Here are some samples.”

- *Playful*:  
  “Hey assistant! Sound just like me — casual, quirky, and don’t forget the emojis 😉.”

- *Professional*:  
  “You're helping a busy professional. Be clear, concise, and match my typical email tone.”

---

## 🧪 Coming Soon

Planned features for the Streamlit interface:
- ✨ Better display and rating of prompt variants
- 💾 In-app saving to `saved_prompts.json`
- ⚙️ Improved error handling for API failures and missing configs
- 🧠 Sidebar with usage tips and app version
- 🔁 Prompt regeneration and reset buttons
- 📊 Optional feedback on token usage and performance
