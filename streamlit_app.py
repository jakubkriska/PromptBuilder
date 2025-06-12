

"""
Streamlit UI for PromptBuilder
Author: Jakub Kriska
"""

import os
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from evaluator import log_evaluation

# Local helpers
from utils import load_templates, save_output

# --------------------------------------------------
# Environment & client setup
# --------------------------------------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ No GROQ_API_KEY found. Add it to a .env file in the project root.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

# Supported Groq models (update as needed)
MODEL_OPTIONS = {
    "LLaMA‑3 8B": "llama3-8b-8192",
    "LLaMA‑3 70B": "llama3-70b-8192",
    "Gemma2 9B IT": "gemma2-9b-it",
    "LLaMA-3.3 70B": "llama-3.3-70b-versatile",
}

# --------------------------------------------------
# Streamlit layout
# --------------------------------------------------
st.set_page_config(page_title="PromptBuilder UI", page_icon="🧠", layout="centered")
st.title("🧠 PromptBuilder — Playground")

with st.sidebar:
    st.header("⚙️ Settings")
    model_label = st.selectbox("Groq model", list(MODEL_OPTIONS.keys()))
    model_name = MODEL_OPTIONS[model_label]
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.05)
    show_prompts = st.checkbox("Show prompt templates", value=False)

# ------------------------------------------------------------------
# Main input
# ------------------------------------------------------------------
st.subheader("Describe your task")
user_task = st.text_area(
    "E.g. ‘Summarize this article in 3 bullet points’ or ‘Generate an image prompt for a dwarf warrior’",
    height=120,
)

# ------------------------------------------------------------------
# Generate prompt variants
# ------------------------------------------------------------------
if user_task and st.button("Generate variants"):
    templates = load_templates()
    st.info("Generating prompt variants …")

    for idx, template in enumerate(templates, start=1):
        prompt = template.replace("{{task}}", user_task)

        if show_prompts:
            with st.expander(f"Prompt Variant {idx}"):
                st.code(prompt, language="text")

        # LLM call
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
            )
            output_text = response.choices[0].message.content
        except Exception as err:
            output_text = f"⚠️ LLM error: {err}"
            st.error(output_text)

        # Display result
        st.markdown(f"### 🎯 Variant {idx}")
        st.write(output_text)

        # Persist to log
        save_output(user_task, prompt, output_text)

    st.success("Done! All variants generated and logged.")

# --- User evaluation section ---
st.markdown("---")
st.subheader("Evaluate the Output")

selected_variant = st.radio(
    "Which output did you prefer?",
    ("Variant 1", "Variant 2", "Variant 3"),
    key="selected_variant"
)
if st.button("Submit Selection"):
    st.success(f"✅ You selected {selected_variant}")
    log_evaluation(selected_variant)

st.markdown("---")
st.caption(
    "Built with ❤️ by Jakub Kriska · PromptBuilder lets you iterate quickly on prompt ideas and compare responses across Groq models."
)