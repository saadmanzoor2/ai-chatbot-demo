import streamlit as st
from groq import Groq

# Create the Groq client using the API key stored in .streamlit/secrets.toml
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Configure the browser tab title and icon
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("AI Chatbot")

# Initialize chat memory (only runs once, on the very first app load)
# st.session_state persists data across Streamlit reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# Redraw the full chat history on every rerun so past messages stay visible
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Show a chat input box at the bottom of the page
user_input = st.chat_input("Type your message...")

if user_input:
    # Save the user's message to memory
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Immediately display the user's message
    with st.chat_message("user"):
        st.write(user_input)

    # Send the full conversation history to the AI and get a response
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # fast model, good for demos
            messages=st.session_state.messages,  # full history = AI remembers context
            stream=True  # get the reply in small chunks as it's generated
        )
        # Display the reply live, chunk by chunk, like a typing effect
        reply = st.write_stream(
            chunk.choices[0].delta.content or ""
            for chunk in response
        )

    # Save the AI's full reply to memory so future messages have context
    st.session_state.messages.append({"role": "assistant", "content": reply})
