# 🤖 AI Chatbot

A simple, fast AI chatbot built with Streamlit and the Groq API. Features real-time streaming responses and conversation memory.

🔗 **Live Demo:** [ai-chatbot-demo.streamlit.app](https://ai-chatbot-demo-ccdpscq9jjjghxjpf4wjzg.streamlit.app/)

## Features

-  Real-time streaming responses (word-by-word, like ChatGPT)
-  Conversation memory — remembers context within a session
-  Powered by Groq's fast LLM inference (Llama 3.1)
-  Clean, simple chat interface

## Tech Stack

- **Frontend/Backend:** Streamlit
- **AI Provider:** Groq API (Llama 3.1 8B Instant)
- **Language:** Python

## Run Locally

1. Clone the repo:
```bash
   git clone https://github.com/saadmanzoor2/ai-chatbot-demo.git
   cd ai-chatbot-demo
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Add your Groq API key in `.streamlit/secrets.toml`:
```toml
   GROQ_API_KEY = "your_api_key_here"
```

4. Run the app:
```bash
   streamlit run app.py
```

## About

Built by [Saad Manzoor](https://github.com/saadmanzoor2) as a demo project for freelance chatbot development.
