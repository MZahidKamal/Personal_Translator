# 🌐 Banglish Personal Translator

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B.svg)
![Gemini AI](https://img.shields.io/badge/Gemini%20AI-3--flash--preview-orange.svg)

A high-performance, AI-powered translation application that bridges the gap between **Banglish** (Bengali written in Roman script) and major languages like **English**, **German**, and proper **Bengali script**. Built for recruiters, travelers, and linguists who need quick, formal, and accurate translations.

🔗 **Live Demo:** [personaltranslator-deb.streamlit.app](https://personaltranslator-deb.streamlit.app/)

---

## 🔥 Key Features

- **Multi-Target Translation:** Supports seamless conversion from Banglish to English, German, and Bengali Script.
- **Smart Prompt Engineering:** Powered by the cutting-edge `gemini-3-flash-preview` model for context-aware and formal output.
- **Modern UI/UX:** Clean, responsive interface built with Streamlit, including a character-limited input area (1,000 chars).
- **One-Click Experience:** Features a built-in code block display for easy copying and a smart 'Clear Input' functionality using session state callbacks.
- **Security First:** Implements environment variable management (`.env`) to keep API credentials secure.

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **AI Core:** [Google Gen AI SDK](https://github.com/google-gemini/generative-ai-python) (Model: `gemini-3-flash-preview`)
- **Environment Management:** `python-dotenv`
- **Language:** Python 3.x

---

## 🚀 Getting Started

Follow these steps to run the project locally on your machine.

### 1. Prerequisites
Ensure you have Python installed. You will also need a **Gemini API Key**.

### 2. Clone the Repository
```bash
git clone [https://github.com/your-username/personal-translator.git](https://github.com/your-username/personal-translator.git)
cd personal-translator
```

### 3. Install Dependencies
```bash
pip install streamlit google-genai python-dotenv
```

### 4. Setup Environment Variables
Create a file named `.env` in the root directory and add your API key:
```text
GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Run the Application
```bash
streamlit run my_translator.py
```

---

## 💡 How It Works

1. **Input:** User enters up to 1,000 characters of Banglish text.
2. **Selection:** Choose the target language (German, English, or Bangla).
3. **Processing:** The app sends a highly-tuned system prompt along with the user input to the Gemini AI model.
4. **Output:** The translated text is rendered inside a clean, copyable code block.

---

## 🛡️ Edge Case Handling

- **Validation:** The app intelligently detects empty inputs or unselected languages and provides user-friendly warnings.
- **State Management:** Uses specialized callback functions to clear inputs without triggering Streamlit's session state errors.
- **Error Handling:** Robust try-except blocks handle potential API or connection failures gracefully.

---

## 👤 Author

* **[Mohammad Zahid Kamal]** *Full Stack AI Enthusiast & Developer*
* *LinkedIn* [https://www.linkedin.com/in/md-zahid-kamal/]
* *Portfolio* [https://md-zahid-kamal.vercel.app/]

---
*Developed with ❤️ as part of an AI Exploration Project.*

