import streamlit as st

# Setup premium wide layout
st.set_page_config(page_title="CoreAI Solutions | Enterprise AI Agency", layout="wide", initial_sidebar_state="expanded")

# --- ADVANCED FANCY CSS WITH SCREEN ANIMATIONS ---
st.markdown("""
    <style>
    /* Import modern tech font */
    @import url('https://googleapis.com');
    
    * { font-family: 'Space Grotesk', sans-serif; }
    
    /* Smooth fade-in animation for the whole screen */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .animated-hero {
        animation: fadeIn 1.2s ease-out;
    }
    
    /* Glowing Glassmorphism Card Style */
    .fancy-card {
        padding: 30px;
        border-radius: 16px;
        background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(240,244,248,0.9) 100%);
        border: 1px solid rgba(43, 108, 176, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.06);
        margin-bottom: 20px;
        transition: all 0.3s ease-in-out;
    }
    
    /* Fancy Hover effect: Card lifts up and glows blue when mouse moves over it! */
    .fancy-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 40px 0 rgba(43, 108, 176, 0.15);
        border: 1px solid rgba(43, 108, 176, 0.5);
    }
    
    .main-title { 
        font-size: 52px; 
        font-weight: 700; 
        background: linear-gradient(45deg, #1A365D, #2B6CB0, #3182CE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px; 
    }
    
    .sub-title { font-size: 22px; color: #4A5568; margin-bottom: 30px; line-height: 1.6; }
    .section-bar { font-size: 28px; font-weight: 600; color: #1A365D; margin-top: 40px; margin-bottom: 25px; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR IDENTIFIER ---
try:
    st.sidebar.image("logo.png", width=190)
except:
    st.sidebar.image("https://icons8.com", width=80)
st.sidebar.title("CoreAI Solutions")
st.sidebar.caption("⚡ Next-Generation Automation")

# --- MAIN ANIMATED HERO LAYOUT ---
st.markdown("<div class='animated-hero'>", unsafe_allow_html=True)

st.markdown("<div class='main-title'>COREAI SOLUTIONS</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>We engineer autonomous, hyper-realistic conversational brains that handle customer support and capture business revenue 24/7.</div>", unsafe_allow_html=True)

# Premium corporate banner image
st.image("https://unsplash.com", use_container_width=True)

st.markdown("<div class='section-bar'>🚀 Our Enterprise Capabilities</div>", unsafe_allow_html=True)

# 3-Column layout with interactive hovering cards
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<div class='fancy-card'>
    <h3 style='color: #2B6CB0; margin-top:0;'>💬 Conversational Clarity</h3>
    <p style='color: #4A5568; font-size: 15px;'>Instantly processes complex client inquiries regarding pricing models, operational rules, and services with zero delay.</p>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class='fancy-card'>
    <h3 style='color: #2B6CB0; margin-top:0;'>📈 Autonomous Lead Capture</h3>
    <p style='color: #4A5568; font-size: 15px;'>Isolates user buying patterns mid-chat to securely extract names, emails, and phone numbers directly into your private database.</p>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class='fancy-card'>
    <h3 style='color: #2B6CB0; margin-top:0;'>💸 Zero Upkeep Architecture</h3>
    <p style='color: #4A5568; font-size: 15px;'>Engineered over highly optimized cloud server structures, completely eliminating monthly maintenance bills.</p>
    </div>""", unsafe_allow_html=True)

st.markdown("<div class='section-bar'>🌟 Why Partner With Our Agency?</div>", unsafe_allow_html=True)
st.markdown("""
<div style='background-color: #F8FAFC; padding: 25px; border-radius: 12px; border-left: 4px solid #2B6CB0;'>
    <p style='font-size: 16px; color: #2D3748; line-height: 1.7; margin: 0;'>
    Modern businesses lose massive revenue because of delayed responses outside regular working hours. 
    <b>CoreAI Solutions</b> bridges this gap by deploying custom, ultra-responsive digital assistants tailored to your industry rules. 
    We replace static online contact forms with live, high-converting pipelines. Navigate to our interactive showrooms in the sidebar to experience the future of business automation.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True) # Close animated-hero div
