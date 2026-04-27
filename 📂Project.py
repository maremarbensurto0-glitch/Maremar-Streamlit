import streamlit as st

st.title("📂 My Projects")

projects ={
    "E- Attendance Navigator":"📊 Attendance system with respects.",
    "SAOD Web App": "🛒 Promote local products.",
    "Banking system": "🏦 Handles transaction and analytics."
}

for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)