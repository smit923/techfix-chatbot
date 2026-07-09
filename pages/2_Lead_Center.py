import streamlit as st

# FIX 1: Removed st.set_page_config to completely prevent multi-page routing layout crashes!

st.markdown("# 📊 Centralized Customer Databases")
st.markdown("### Secure access panel for business owners to download collected text leads.")
st.write("---")

# Maintain a unified session storage namespace matching your showroom page configuration
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
        # Render dynamic leads collected from either manual entry or automated live showroom prompts
        for index, lead in enumerate(st.session_state.leads, 1):
            st.info(f"🗃️ **Record Reference #{index}:** {lead['name'].upper()} — 📱 Contact: {lead['phone']}")
            
        # Recruiter Proof Bonus: Convert dictionary state to a clean CSV data stream for business utility downloads
        import csv
        from io import StringIO
        
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["Index", "Customer Name", "Phone Number"])
        for idx, item in enumerate(st.session_state.leads, 1):
            writer.writerow([idx, item["name"], item["phone"]])
        csv_data = output.getvalue()
        
        st.download_button(
            label="📥 Download Database Logs (CSV)",
            data=csv_data,
            file_name="coreai_solutions_leads.csv",
            mime="text/csv",
            use_container_width=True
        )
    else:
        st.caption("Database pipelines are currently empty. Run customer conversations on the Live Demos page to log data.")
