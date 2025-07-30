import streamlit as st

st.set_page_config(page_title="FPL Draft Dashboard", layout="wide")

st.title("FPL Draft League Dashboard")

st.markdown("Use the sidebar to navigate to different views:")
st.sidebar.page_link("pages/League_Overview.py", label="League Overview")
st.sidebar.page_link("pages/Cup_Tracker.py", label="Cup Tracker")
st.sidebar.page_link("pages/H2H_Fixtures.py", label="H2H Fixtures")

import streamlit as st

st.set_page_config(page_title="FPL Draft Dashboard", layout="wide")

st.title("Welcome to the FPL Draft Dashboard 🚀")

st.markdown("""
Navigate through the pages on the left sidebar:
- **League Overview**
- **Cup Tracker**
- **H2H Fixtures**
""")
