
import streamlit as st
from google import genai
from google.genai import types

st.title("🚀 Free Automated Customer Support Bot")
st.write("Powered by Google Gemini — 100% Free Tier!")

# Sidebar for Google's API key
api_key = st.sidebar.text_input("Enter Google Gemini API Key", type="password")

if api_key:
    # Connect to Google's AI brain
    client = genai.Client(api_key=api_key)

    system_instruction = (
        "You are an expert customer service agent for TechFix Repairs. "
        "We fix cracked phone screens for ₹4,000 and replace laptop batteries for ₹6,000. "
        "We are open Monday to Friday from 9 AM to 6 PM. We offer a 6-month warranty. "
        "Be extremely polite, professional, and try to get the customer to book an appointment."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display past messages safely mapping 'model' to 'assistant' layout for visual neatness
    for message in st.session_state.messages:
        display_role = "assistant" if message["role"] == "model" else "user"
        st.chat_message(display_role).write(message["content"])

    user_input = st.chat_input("Type your question here...")

    if user_input:
        # Show what user typed
        st.chat_message("user").write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Format history perfectly using Google's rules ('user' and 'model')
        history = [types.Content(role=m["role"], parts=[types.Part.from_text(text=m["content"])]) for m in st.session_state.messages[:-1]]
        
        # Start chat session
        chat = client.chats.create(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
            ),
            history=history
        )
        
        # Send message and receive response
        response = chat.send_message(user_input)
        ai_reply = response.text
        
        # Show and save reply with the correct 'model' role
        st.chat_message("assistant").write(ai_reply)
        st.session_state.messages.append({"role": "model", "content": ai_reply})
else:
    st.info("Please enter your Google Gemini API key in the sidebar.")
