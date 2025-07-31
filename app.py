import streamlit as st

st.set_page_config(page_title="FPL Draft Dashboard", layout="wide")

st.title("FPL Draft League Dashboard")

st.markdown("Use the sidebar to navigate to different views:")
st.sidebar.page_link("pages/League_Overview.py", label="Manager Overview")
st.sidebar.page_link("pages/Cup_Tracker.py", label="Cup Tracker")
st.sidebar.page_link("pages/H2H_Fixtures.py", label="Statistics")

import streamlit as st

st.set_page_config(page_title="FPL Draft Dashboard", layout="wide")

st.title("Welcome to the FPL Draft Dashboard 🚀")

st.markdown("""
Navigate through the pages on the left sidebar:
- **Manager Overview**
- **Cup Tracker**
- **Statistics**
""")
