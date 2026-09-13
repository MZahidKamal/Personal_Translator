import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv


# 1. Configuration and API Setup
load_dotenv()
groq_api_key = os.getenv("GROQ_CLOUD_API_KEY")
groq_model_name = os.getenv("GROQ_CLOUD_OPENAI_MODEL")

# 2. Model Setup
model = ChatGroq(model=groq_model_name, groq_api_key=groq_api_key, temperature=0.0)
parser = StrOutputParser()


# 3. Set Page Configuration
st.set_page_config(page_title="Personal Translator", page_icon="🌐")


# 4. Define Translation Prompts
prompt_instruction_for_german = ("Translate the following Banglish text into formal German."
                     "No introduction, no conclusion, no extra context, no extra feature, no change of tone, no change of style, no change of sentence structure, no change of emotion."
                     "If the input is formal then translate in German using formal tone."
                     "If the input is informal then translate in German using informal tone."
                     "Only use A1 or maximum A2 level German translation and style: ")

prompt_instruction_for_english = ("Translate the following Banglish text into fluent English."
                      "No introduction, no conclusion, no extra context, no extra feature, no change of tone, no change of style, no change of sentence structure, no change of emotion."
                      "If the input is formal then translate in English using formal tone."
                      "If the input is informal then translate in English using informal tone."
                      "Only simply translate in English using natural style: ")

prompt_instruction_for_bangla = ("Convert the following Banglish text into proper Bengali (Bangla) script."
                     "No introduction, no conclusion, no extra context, no extra feature, no change of tone, no change of style, no change of sentence structure, no change of emotion."
                     "Only simply convert in Bangla script using bangla font using same tone and style: ")

# 5. Prompt Templates
german_prompt = PromptTemplate.from_template(f"{prompt_instruction_for_german}"+"\n{text}")
english_prompt = PromptTemplate.from_template(f"{prompt_instruction_for_english}"+"\n{text}")
bangla_prompt = PromptTemplate.from_template(f"{prompt_instruction_for_bangla}"+"\n{text}")


# 6. Now we'll run all three translation branches AT THE SAME TIME, using RunnableParallel.
parallel_translation_chain = RunnableParallel(
    german=german_prompt | model | parser,
    english=english_prompt | model | parser,
    bangla=bangla_prompt | model | parser,   # FIX: key renamed to 'bangla' to match how it's read below
)


# 7. Define a callback function to clear the input
def clear_text():
    st.session_state["banglish_input"] = ""


# 8. UI Layout
st.title("🌐 Personal Translator")
st.write("Welcome! Convert your Banglish sentences into German, English, or proper Bangla.")


# 9. Text Input with 1000-character limit
user_input = st.text_area(
    "Enter Banglish Text:",
    max_chars=1000,
    placeholder="e.g., as salamu alaikum...",
    key="banglish_input"
)

# 10. Submit and Clear Buttons
col1, col2 = st.columns(2)
with col1:
    submit_clicked = st.button("Submit")
with col2:
    st.button("Clear", on_click=clear_text)


# 11. Final Checks and Translations
if submit_clicked:
    if not user_input or not user_input.strip():
        st.warning("Please enter some text in Banglish first!")
    else:
        try:
            with st.spinner("Translating for you..."):

                # FIX: use the REAL user_input instead of a hardcoded string.
                result = parallel_translation_chain.invoke({"text": user_input})

                translated_german_text = result["german"]
                translated_english_text = result["english"]
                translated_bangla_text = result["bangla"]

                # Display Results
                st.markdown("---")
                st.subheader("Translated Output:")

                st.markdown("**German:**")
                st.code(translated_german_text, language=None)

                st.markdown("**English:**")
                st.code(translated_english_text, language=None)

                st.markdown("**Bangla:**")
                st.code(translated_bangla_text, language=None)

                st.markdown("---")

        except Exception as e:
            st.error(f"Translation failed: {str(e)}")
