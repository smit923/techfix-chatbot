import streamlit as st

# Setup page layout
st.set_page_config(page_title="CoreAI Solutions | Corporate", layout="wide", initial_sidebar_state="expanded")

# --- BRANDING BLOCK ---
st.markdown("""
    <style>
    .main-title { font-size: 46px; font-weight: bold; color: #1A365D; margin-bottom: 2px; }
    .sub-title { font-size: 22px; color: #4A5568; margin-bottom: 25px; }
    .feature-box { padding: 25px; border-radius: 12px; background-color: #F7FAFC; border-left: 6px solid #2B6CB0; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .section-bar { font-size: 26px; font-weight: bold; color: #2B6CB0; margin-top: 35px; margin-bottom: 20px; border-bottom: 3px solid #E2E8F0; padding-bottom: 8px; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR IDENTIFIER ---
try:
    st.sidebar.image("logo.png", width=180)
except:
    st.sidebar.image("https://icons8.com", width=80)
st.sidebar.title("CoreAI Solutions")
st.sidebar.caption("Next-Gen Conversational Automation")

# --- MAIN HERO LAYOUT ---
st.markdown("<div class='main-title'>⚡ COREAI SOLUTIONS</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>We engineer autonomous conversational agents that manage customer communication and capture business leads 24/7.</div>", unsafe_allow_html=True)

st.image("https://unsplash.com", caption="CoreAI Global Enterprise Networks", use_container_width=True)

st.markdown("<div class='section-bar'>Our Enterprise Capabilities</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<div class='feature-box'>
    <h3>💬 Intelligent FAQ Systems</h3>
    <p>Instantly answers repetitive client queries regarding pricing metrics, operating schedules, warranties, and locations.</p>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class='feature-box'>
    <h3>📈 Predictive Lead Generation</h3>
    <p>Automatically isolates booking intents from chat patterns to capture customer contact parameters with precision.</p>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class='feature-box'>
    <h3>💸 Optimized Infrastructure</h3>
    <p>Built directly over cloud-native free tier structures, completely eliminating monthly server maintenance bills.</p>
    </div>""", unsafe_allow_html=True)

st.markdown("<div class='section-bar'>Why Work With Our Agency?</div>", unsafe_allow_html=True)
st.write(
    "CoreAI Solutions builds custom conversational brains tailored to your specific industry constraints. "
    "We replace slow web forms with active, real-time sales pipelines that interact with visitors in a human voice. "
    "Use the sidebar menu to navigate to our live interactive showrooms and test our automated engines."
)
