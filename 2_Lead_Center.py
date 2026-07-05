import streamlit as st

st.set_page_config(page_title="CoreAI Solutions | Dashboard", layout="wide")

st.markdown("# 📊 Centralized Customer Databases")
st.markdown("### Secure access panel for business owners to download collected text leads.")
st.write("---")

if "leads" not in st.session_state:
    st.session_state.leads = []
    
col_input, col_grid = st.columns(2)

with col_input:
    st.markdown("### 📝 Manual System Entry")
    with st.form("add_lead_form", clear_on_submit=True):
        name = st.text_input("Customer Name Reference")
        phone = st.text_input("Customer Phone Number")
        clicked = st.form_submit_button("Commit Data Stream")
        if clicked and name and phone:
            st.session_state.leads.append({"name": name, "phone": phone})
            st.success("Lead parameters saved successfully!")

with col_grid:
    st.markdown("### 💾 Live Server Storage")
    if st.session_state.leads:
        for index, lead in enumerate(st.session_state.leads, 1):
            st.info(f"🗃️ **Record Reference #{index}:** {lead['name'].upper()} — 📱 Contact: {lead['phone']}")
    else:
        st.caption("Database pipelines are currently empty. Run customer conversations on the Live Demos page to log phone data.")
