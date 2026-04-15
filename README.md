# 🌐 Banglish Personal Translator

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B.svg)
![Gemini AI](https://img.shields.io/badge/Gemini%20AI-3--flash--preview-orange.svg)

A high-performance, AI-powered translation application that bridges the gap between **Banglish** (Bengali written in Roman script) and major languages like **English**, **German**, and proper **Bengali script**. Built for recruiters, travelers, and linguists who need quick, formal, and accurate translations.

🔗 **Live Demo:** [www.personaltranslator.streamline.com](http://www.personaltranslator.streamline.com)

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
