import streamlit as st
from google import genai
from google.genai import types

st.title("🚀 Free Automated Customer Support Bot")
st.write("Powered by Google Gemini — 100% Free Tier!")

# AUTOMATIC SECRET KEY CHECK
# Reads the key silently from cloud secrets so users never see it!
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    api_key = st.sidebar.text_input("Enter Google Gemini API Key", type="password")

if api_key:
    try:
        client = genai.Client(api_key=api_key)

        system_instruction = (
            "You are an expert customer service agent for TechFix Repairs. "
            "We fix cracked phone screens for ₹4,000 and replace laptop batteries for ₹6,000. "
            "We are open Monday to Friday from 9 AM to 6 PM. We offer a 6-month warranty. "
            "Be extremely polite, professional. "
            "CRITICAL RULE: Whenever a customer wants to fix a device or book an appointment, "
            "you MUST ask for their Full Name and Phone Number."
        )

        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "leads" not in st.session_state:
            st.session_state.leads = []

        for message in st.session_state.messages:
            st.chat_message(message["role"]).write(message["content"])

        user_input = st.chat_input("Type your question here...")

        if user_input:
            st.chat_message("user").write(user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                ),
            )
            ai_reply = response.text
            
            st.chat_message("assistant").write(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    except Exception as e:
        st.error(f"❌ Connection Error: Details: {e}")

    # SIDEBAR FEATURE: Display collected leads for the owner
    st.sidebar.markdown("---")
    st.sidebar.subheader("📥 Collected Business Leads")
    
    if st.session_state.leads:
        for idx, lead in enumerate(st.session_state.leads, 1):
            st.sidebar.info(f"**Lead #{idx}:** {lead['name']} - {lead['phone']}")
    else:
        st.sidebar.caption("No customer details saved yet.")
else:
    st.info("Please enter your Google Gemini API key or add it to Streamlit Secrets.")
