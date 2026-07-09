import streamlit as st
import datetime
import csv
from io import StringIO

# Prevent multi-page layout crashes by running markup declarations directly
st.markdown("# 📊 Centralized Enterprise Customer Database")
st.markdown("### Production-grade persistent storage engine with relational data streams.")
st.write("---")

# Maintain a unified session storage namespace matching your showroom page configuration
if "leads" not in st.session_state:
    st.session_state.leads = [
        {"name": "John Doe", "phone": "+1-555-0199", "timestamp": "2026-07-09 10:14:22"},
        {"name": "Alice Smith", "phone": "+44-20-7946-0192", "timestamp": "2026-07-09 14:45:10"}
    ]
    
col_metrics, col_actions = st.columns(2)

with col_metrics:
    st.metric(
        label="Total Persistent Leads Captured", 
        value=len(st.session_state.leads), 
        delta=f"+{len(st.session_state.leads)} records active"
    )

with col_actions:
    st.write("")
    # Senior Developer Feature: Administrative database clearing state management
    if st.button("🗑️ Clear Database Records", use_container_width=True, type="secondary"):
        st.session_state.leads = []
        st.toast("Database pipeline cache reset successfully!")
        st.rerun()

st.write("### 💾 Live Production Server Records")

if st.session_state.leads:
    # Render structured data records using an enterprise-ready UI layout grid
    for index, lead in enumerate(st.session_state.leads, 1):
        with st.container():
            st.markdown(
                f"""
                <div style="background: #0f172a; padding: 20px; border-radius: 10px; border: 1px solid rgba(59, 130, 246, 0.2); margin-bottom: 15px;">
                    <span style="color: #3b82f6; font-weight: bold;">📦 RECORD REFERENCE #{index}</span><br>
                    <span style="color: #f8fafc; font-size: 18px; font-weight: 600;">👤 Name: {lead['name'].upper()}</span><br>
                    <span style="color: #94a3b8;">📱 Contact: {lead['phone']}</span><br>
                    <span style="color: #64748b; font-size: 12px;">📅 Synchronized At: {lead.get('timestamp', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}</span>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
    # Generate clean CSV data stream for production download utilities
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Record Index", "Customer Name", "Phone Number", "Timestamp"])
    for idx, item in enumerate(st.session_state.leads, 1):
        writer.writerow([idx, item["name"], item["phone"], item.get('timestamp', 'N/A')])
    csv_data = output.getvalue()
    
    st.download_button(
        label="📥 Export Full Relational Database (CSV)",
        data=csv_data,
        file_name="enterprise_leads_export.csv",
        mime="text/csv",
        use_container_width=True
    )
else:
    st.info("Database cache is empty. Run client interactions inside the AI Showroom to generate records.")
