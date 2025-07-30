import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Read the service account info from Streamlit secrets
service_account_info = st.secrets["gcp_service_account"]
creds = Credentials.from_service_account_info(service_account_info, scopes=scope)

# Authorize gspread client
client = gspread.authorize(creds)

# Open your Google Sheet
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/11kPu3L7MlgQXF6r5SLPhQ9Msie-iDEm61c1vi4hvrag/edit")

# Fetch manager tabs (tabs 2 to 11)
manager_tabs = spreadsheet.worksheets()[1:11]
manager_names = [ws.title for ws in manager_tabs]

# Sidebar Selectbox
selected_manager = st.sidebar.selectbox("Select Manager", manager_names)

# Load Selected Manager's Data
ws = spreadsheet.worksheet(selected_manager)
raw_data = ws.get_all_values()

# Ensure we have data
if not raw_data or len(raw_data) < 2:
    st.error("No data found or sheet is improperly formatted.")
else:
    headers = raw_data[0]
    headers = [h if h != '' else f'Unnamed_{i}' for i, h in enumerate(headers)]
    
    df = pd.DataFrame(raw_data[1:], columns=headers)

    # Try converting numeric columns
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')

    st.title(f"{selected_manager} - Season Results")
    st.dataframe(df)

    # Example Visualizations
    if 'GW' in df.columns and 'Points' in df.columns:
        df_sorted = df.sort_values(by='GW')
        st.line_chart(df_sorted.set_index('GW')['Points'])

        total_pts = df['Points'].sum()
        avg_pts = df['Points'].mean()
        st.metric("Total Points", total_pts)
        st.metric("Average per GW", f"{avg_pts:.2f}")
    else:
        st.warning("No 'GW' or 'Points' columns found for graphing.")
