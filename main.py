import streamlit as st
from google import genai
import os
from dotenv import load_dotenv


# 1. Configuration and API Setup
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
gemini_model = os.getenv("GEMINI_MODEL")


# Initialize Gemini Client
client = None
if api_key:
    client = genai.Client(api_key=api_key)


# Set Page Configuration
st.set_page_config(page_title="Personal Translator", page_icon="🌐")


# 2. Define Translation Prompts (Backend Updates)
prompt_for_german = ("Translate the following Banglish text into formal German."
                     "No introduction, no conclusion, no extra context, no extra feature, no change of tone, no change of style, no change of sentence structure, no change of emotion."
                     "If the input is formal then translate in German using formal tone."
                     "If the input is informal then translate in German using informal tone."
                     "Only use A1 or maximum A2 level German translation and style: ")

prompt_for_english = ("Translate the following Banglish text into fluent English."
                      "No introduction, no conclusion, no extra context, no extra feature, no change of tone, no change of style, no change of sentence structure, no change of emotion."
                      "If the input is formal then translate in English using formal tone."
                      "If the input is informal then translate in English using informal tone."
                      "Only simply translate in English using natural style: ")

prompt_for_Bangla = ("Convert the following Banglish text into proper Bengali (Bangla) script."
                     "No introduction, no conclusion, no extra context, no extra feature, no change of tone, no change of style, no change of sentence structure, no change of emotion."
                     "Only simply convert in Bangla script using bangla font using same tone and style: ")

PROMPTS = {
    "German": prompt_for_german,
    "English": prompt_for_english,
    "Bangla": prompt_for_Bangla
}


# Define a callback function to clear the input
def clear_text():
    st.session_state["banglish_input"] = ""


# 3. UI Layout
st.title("🌐 Personal Translator")
st.write("Welcome! Convert your Banglish sentences into German, English, or proper Bangla.")


# Text Input with 1000-character limit
user_input = st.text_area(
    "Enter Banglish Text:",
    max_chars=1000,
    placeholder="e.g., as-salamu-alaikum...",
    key="banglish_input"
)


# Language selection with Radio buttons
selected_language = st.radio(
    "Select Target Language:",
    options=["German", "English", "Bangla"],
    index=None
)


# Layout for Buttons
col1, col2 = st.columns([1, 5])
with col1:
    translate_button = st.button("Translate")
with col2:
    # Use callback to clear the text area safely
    st.button("Clear Input", on_click=clear_text)


# 4. Logic and Conditional Rendering
if translate_button:
    # Edge Case: Check if text input is empty
    if not user_input.strip():
        st.warning("Please enter some text in Banglish first!")

    # Edge Case: Check if language is selected
    elif selected_language is None:
        st.warning("Please select a target language!")

    # Edge Case: API Key validation
    elif not client:
        st.error("API Key missing! Please check your .env file.")

    else:
        try:
            with st.spinner(f"Translating to {selected_language}..."):
                # Construct prompt from backend dictionary
                final_prompt = f"{PROMPTS[selected_language]}\n\nText: {user_input}"

                # Call Gemini API
                response = client.models.generate_content(
                    model=gemini_model,
                    contents=final_prompt
                )

                translated_text = response.text

                # Display Results
                st.markdown("---")
                st.subheader("Translated Output:")

                # Displaying the result inside a code block with bash syntax
                st.code(f"{translated_text}", language="bash")

                st.markdown("---")

        except Exception as e:
            st.error(f"Translation failed: {str(e)}")
