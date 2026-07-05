import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="CoreAI Solutions | Live Demos", layout="wide")

st.markdown("# 🛠️ Interactive AI Showroom")
st.markdown("### Select an industry below to test our custom virtual business assistants in real time.")
st.write("---")

if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    api_key = st.sidebar.text_input("Developer Authentication Key", type="password")

if api_key:
    try:
        client = genai.Client(api_key=api_key)

        bot_mode = st.selectbox(
            "Choose a business assistant to chat with:",
            ["Best Western Plus (Ardmore, Oklahoma USA)", "Grand Plaza Hotel (USA Hospitality)", "TechFix Repairs (Mobile/Laptop Hub)", "Elite Fitness Gym Center", "Sparkle Dental Care Clinic"]
        )

        if bot_mode == "Best Western Plus (Ardmore, Oklahoma USA)":
            system_instruction = (
                "You are an expert, elite virtual front desk concierge for the Best Western Plus Ardmore Inn & Suites in Oklahoma, USA. "
                "We provide clean, comfortable rooms, free high-speed Wi-Fi, free hot breakfast, a modern fitness center, and a beautiful indoor pool with a hot tub. "
                "Check-in time is exactly 3:00 PM and check-out time is 12:00 PM. We are a 100% smoke-free and pet-free property. "
                "Always maintain an incredibly polite, welcoming, helpful, and highly professional American hospitality tone. "
                "CRITICAL RULE: Whenever a guest wants to book a room, check room availability, or plan a stay, "
                "you MUST politely ask for their Full Name, Phone Number, and Email Address to process their reservation log."
            )
        elif bot_mode == "Grand Plaza Hotel (USA Hospitality)":
            system_instruction = (
                "You are an expert, world-class virtual concierge for The Grand Plaza Hotel in Miami, USA. "
                "Standard rooms start at $149 per night, and luxury suites are $299 per night. Check-in is 3 PM, check-out is 11 AM. "
                "Always sound extremely welcoming, helpful, and high-end. "
                "CRITICAL RULE: Whenever a guest asks to book a room or check availability, "
                "you MUST ask for their Full Name, Phone Number, and Email Address to lock in their reservation details."
            )
        elif bot_mode == "TechFix Repairs (Mobile/Laptop Hub)":
            system_instruction = (
                "You are an expert customer service agent for TechFix Repairs store. "
                "We fix cracked phone screens for ₹4,000 and replace laptop batteries for ₹6,000. Open Mon-Fri 9AM-6PM. "
                "Be extremely polite and professional. "
                "CRITICAL RULE: Whenever a customer wants to fix a device or book a slot, "
                "you MUST ask for their Full Name and Phone Number."
            )
        elif bot_mode == "Elite Fitness Gym Center":
            system_instruction = (
                "You are an expert sales representative for Elite Fitness Gym. "
                "Our monthly membership costs ₹1,500. Open 24/7. "
                "Be highly motivating, encouraging, and friendly. "
                "CRITICAL RULE: Whenever a user asks about joining or membership trials, "
                "you MUST ask for their Full Name and Phone Number to secure their free trial pass."
            )
        elif bot_mode == "Sparkle Dental Care Clinic":
            system_instruction = (
                "You are a professional medical receptionist for Sparkle Dental Care clinic. "
                "A standard checkup costs ₹800. Open Mon-Sat 10 AM to 8 PM. "
                "Be calm, reassuring, and highly structured. "
                "CRITICAL RULE: Whenever a patient wants to schedule a checkup or book a slot, "
                "you MUST ask for their Full Name and Phone Number to look up open dental slots."
            )

        if "current_bot" not in st.session_state or st.session_state.current_bot != bot_mode:
            st.session_state.current_bot = bot_mode
            st.session_state.messages = []

        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "leads" not in st.session_state:
            st.session_state.leads = []

        for message in st.session_state.messages:
            st.chat_message(message["role"]).write(message["content"])

        user_input = st.chat_input(f"Type a message to test the {bot_mode} assistant...")

        if user_input:
            st.chat_message("user").write(user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input,
                config=types.GenerateContentConfig(system_instruction=system_instruction),
            )
            ai_reply = response.text
            
            st.chat_message("assistant").write(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    except Exception as e:
        st.error(f"❌ Connection Error: {e}")
else:
    st.warning("⚠️ Cloud connection error. Please refresh the page parameters.")
