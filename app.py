import streamlit as st
from groq import Groq

# Create the Groq client using the API key stored in secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Configure the browser tab title and icon
st.set_page_config(page_title="Saad - AI Assistant", page_icon="🤖")
st.title("Saad")
st.caption("Your AI Assistant")

# Sidebar - shows info about the bot and a clear chat button
with st.sidebar:
    st.header("About")
    st.write("Hi, I'm **Saad** — your AI assistant.")
    st.write("I'm here to help answer your questions and assist with whatever you need.")
    st.divider()
    st.caption("Powered by Groq · Llama 3.1")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat memory with a system message so the AI knows its name and tone
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant. Your name is Saad, and you can refer to yourself by that name. If asked directly whether you are an AI, be honest that you are an AI assistant. Keep responses clear, friendly, and professional."}
    ]

# Show a welcome message if this is a fresh conversation (no user messages yet)
if len(st.session_state.messages) == 1:
    st.info("👋 Hello! I'm Saad, your AI assistant. Feel free to ask me anything.")

# Redraw the full chat history (skip the hidden system message)
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    avatar = "🧑" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

# Show a chat input box at the bottom of the page
user_input = st.chat_input("Type your message...")

if user_input:
    # Save the user's message to memory
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="🧑"):
        st.write(user_input)

    # Send the full conversation history to the AI and get a response
    with st.chat_message("assistant", avatar="🤖"):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.messages,
            stream=True
        )
        reply = st.write_stream(
            chunk.choices[0].delta.content or ""
            for chunk in response
        )

    # Save the AI's full reply to memory
    st.session_state.messages.append({"role": "assistant", "content": reply})
