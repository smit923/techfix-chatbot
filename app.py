import streamlit as st

# Force wide page layout structure for an enterprise dashboard experience
st.set_page_config(page_title="CoreAI Solutions | Premium Hospitality Automation", layout="wide", initial_sidebar_state="expanded")

# --- HIGH-END DIGITAL BRAND ARCHITECTURE & KEYFRAME ANIMATIONS ---
st.markdown("""
    <style>
    /* Inject Space Grotesk engineering font */
    @import url('https://googleapis.com');
    * { font-family: 'Space Grotesk', sans-serif; }

    /* Keyframe Animations for Fluid Screen Loading */
    @keyframes slideUpFade {
        0% { opacity: 0; transform: translateY(40px); filter: blur(4px); }
        100% { opacity: 1; transform: translateY(0); filter: blur(0); }
    }
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Container System for Animated Viewport Entry */
    .animated-viewport {
        animation: slideUpFade 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    /* Premium Metallic Shimmer Corporate Title Text */
    .enterprise-title { 
        font-size: 56px; 
        font-weight: 700; 
        letter-spacing: -1.5px;
        background: linear-gradient(-45deg, #0f172a, #2563eb, #1d4ed8, #3b82f6);
        background-size: 300% 300%;
        animation: gradientShift 8s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px; 
    }
    
    .enterprise-subtitle { 
        font-size: 24px; 
        font-weight: 300;
        color: #475569; 
        margin-bottom: 35px; 
        line-height: 1.5;
    }

    /* High-Definition Cybernetic Glassmorphic Grid Cards */
    .cyber-card {
        padding: 35px 25px;
        border-radius: 20px;
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.95) 100%);
        border: 1px solid rgba(37, 99, 235, 0.15);
        box-shadow: 0 10px 30px -10px rgba(15, 23, 42, 0.04);
        margin-bottom: 25px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    /* Smooth Interactive Transform Hook */
    .cyber-card:hover {
        transform: translateY(-10px) scale(1.01);
        box-shadow: 0 20px 40px -15px rgba(37, 99, 235, 0.18);
        border: 1px solid rgba(37, 99, 235, 0.6);
    }

    .card-icon {
        font-size: 32px;
        margin-bottom: 15px;
    }

    .card-title {
        font-size: 22px;
        font-weight: 600;
        color: #0f172a;
        margin-bottom: 12px;
    }

    .card-desc {
        font-size: 15px;
        color: #64748b;
        line-height: 1.6;
        margin: 0;
    }

    /* Elegant Structural Framework Section Break Blocks */
    .glass-showcase {
        background-color: #f8fafc;
        border-left: 5px solid #2563eb;
        padding: 30px;
        border-radius: 16px;
        margin-top: 40px;
        box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.02);
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION SIDEBAR ---
try:
    st.sidebar.image("logo.png", width=190)
except:
    st.sidebar.image("https://icons8.com", width=80)
st.sidebar.title("CoreAI Solutions")
st.sidebar.caption("🛎️ Premium Hospitality AI")

# --- EXECUTE ANIMATED VIEWPORT WRAPPER ---
st.markdown("<div class='animated-viewport'>", unsafe_allow_html=True)

st.markdown("<div class='enterprise-title'>COREAI SOLUTIONS</div>", unsafe_allow_html=True)
st.markdown("<div class='enterprise-subtitle'>We build intelligent 24/7 virtual receptionists for luxury hotels to automate guest support, manage bookings, and increase room sales.</div>", unsafe_allow_html=True)

# Beautiful cinematic hotel reception lobby image instead of generic abstract coding art
st.image("https://unsplash.com", use_container_width=True)

st.markdown("<h2 style='color: #0f172a; font-weight:600; margin-top:40px; margin-bottom:20px;'>🛎️ Smart Hospitality Solutions</h2>", unsafe_allow_html=True)

# 3-Column hotel layout with responsive floating animation nodes
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""<div class='cyber-card'>
    <div class='card-icon'>💬</div>
    <div class='card-title'>Instant Guest Support</div>
    <div class='card-desc'>Instantly handles recurring guest questions regarding check-in times, parking rules, property amenities, and hotel policies with absolute friendly accuracy.</div>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class='cyber-card'>
    <div class='card-icon'>🏨 Direct Room Bookings</div>
    <div class='card-title'>Automated Lead Capture</div>
    <div class='card-desc'>Intelligently guides website visitors through room packages and securely captures guest contact details (Names, Emails, and Phone Numbers) to secure direct bookings.</div>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown("""<div class='cyber-card'>
    <div class='card-icon'>💰 Zero Monthly Software Bills</div>
    <div class='card-title'>Zero Server Overhead</div>
    <div class='card-desc'>Our custom-built frameworks run entirely on highly optimized, cloud-native systems, ensuring your hotel pays exactly zero rupees in monthly upkeep costs.</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #0f172a; font-weight:600; margin-top:30px;'>🌟 Elevate Your Guest Experience</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='glass-showcase'>
    <p style='font-size: 16px; color: #334155; line-height: 1.8; margin: 0;'>
    Modern hotels lose thousands of dollars in room sales when online guests leave the website because of slow email responses or busy front desk phone lines. 
    <b>CoreAI Solutions</b> solves this problem by embedding a custom, highly trained virtual assistant directly onto your website. 
    We turn casual website browsing into guaranteed direct direct guest reservations. Navigate to our interactive showrooms in the sidebar panel to test our live hotel assistants right now.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True) # Terminate animated wrapper layout node
