import streamlit as st

# Force wide enterprise dark layout
st.set_page_config(
    page_title="CoreAI Solutions | Premium Hospitality AI", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- SILICON VALLEY BLACK & NEON GLOW TECH-THEME DESIGN ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }

    /* Force smooth cinematic fade-in slide up */
    @keyframes slideUp {
        0% { opacity: 0; transform: translateY(30px); filter: blur(2px); }
        100% { opacity: 1; transform: translateY(0); filter: blur(0); }
    }
    
    .animated-body {
        animation: slideUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    /* Premium Silicon Valley Dark Card Styles with Neon Blue Glow */
    .silicon-card {
        padding: 35px 25px;
        border-radius: 16px;
        background: #0f172a;
        border: 1px solid rgba(59, 130, 246, 0.2);
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin-bottom: 25px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    /* Interactive Mouse Hover: Glow increases, Card lifts up */
    .silicon-card:hover {
        transform: translateY(-8px);
        border: 1px solid #3b82f6;
        box-shadow: 0 0 25px rgba(59, 130, 246, 0.25);
    }

    .main-brand {
        font-size: 58px;
        font-weight: 700;
        letter-spacing: -1.5px;
        background: linear-gradient(90deg, #3b82f6, #60a5fa, #93c5fd);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    
    .sub-brand {
        font-size: 22px;
        color: #94a3b8;
        margin-bottom: 35px;
        line-height: 1.6;
        font-weight: 300;
    }

    .card-icon { font-size: 36px; margin-bottom: 15px; }
    .card-title { font-size: 22px; font-weight: 600; color: #f8fafc; margin-bottom: 12px; }
    .card-desc { font-size: 15px; color: #94a3b8; line-height: 1.6; margin: 0; }
    
    .hospitality-banner {
        background: linear-gradient(135deg, rgba(15,23,42,0.9), rgba(30,41,59,0.9));
        border-left: 5px solid #3b82f6;
        padding: 30px;
        border-radius: 14px;
        margin-top: 40px;
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

# --- EXECUTE THE ENTIRE ANIMATED STRUCTURAL ENGINE ---
st.markdown("<div class='animated-body'>", unsafe_allow_html=True)

st.markdown("<div class='main-brand'>COREAI SOLUTIONS</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-brand'>Next-generation virtual receptionists custom-engineered for premier global brands like Best Western Plus to automate guest bookings and maximize direct revenue.</div>", unsafe_allow_html=True)

# High-End Luxury Hospitality Header Image
st.image("https://unsplash.com", use_container_width=True)

st.markdown("<h2 style='color: #f8fafc; font-weight:600; margin-top:40px; margin-bottom:25px;'>🛎️ Intellegent Guest Management Infrastructure</h2>", unsafe_allow_html=True)

# 3-Column Luxury Matrix Grid
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""<div class='silicon-card'>
    <div class='card-icon'>💬</div>
    <div class='card-title'>Instant Guest Concierge</div>
    <div class='card-desc'>Instantly handles recurring guest inquiries regarding check-in times, breakfast schedules, indoor pool hours, and amenities with welcoming precision.</div>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class='silicon-card'>
    <div class='card-icon'>🏨 Direct Reservation Locking</div>
    <div class='card-title'>Automated Room Bookings</div>
    <div class='card-desc'>Intelligently detects guest intent mid-chat, answers specific pricing queries, and securely captures Names, Phone Numbers, and Emails to secure direct bookings.</div>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown("""<div class='silicon-card'>
    <div class='card-icon'>💰 Zero Server Overhead</div>
    <div class='card-title'>Cloud-Native Deployment</div>
    <div class='card-desc'>Engineered securely over advanced serverless architecture, completely eliminating monthly platform maintenance fees or upkeep bills.</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #f8fafc; font-weight:600; margin-top:30px;'>🌟 Elevate Your Brand's Guest Experience</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='hospitality-banner'>
    <p style='font-size: 16px; color: #cbd5e1; line-height: 1.8; margin: 0;'>
    Modern hotels lose thousands of dollars in direct room sales when online visitors leave the website due to slow reservation desks or busy phone channels. 
    <b>CoreAI Solutions</b> plugs this revenue leak by deploying highly personalized AI front-desk assistants trained perfectly on your property rules. 
    We turn casual web visitors into guaranteed direct hotel bookings. Use our navigation sidebar panel to enter our interactive showroom and audit our systems.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True) # Terminate animated viewport wrapper node
