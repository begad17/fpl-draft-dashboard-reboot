import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Prepare data
leagueWins = {'Team':['Jordan (1)','Begad (1)','Moe (1)'], 'Championships':[1,1,1]}
df = pd.DataFrame(leagueWins)
teamColours = ['#f40206','#0560b5','#ce0000']  # Must match number of teams!

# Create figure and axis
fig, ax = plt.subplots()
ax.pie(
    df['Championships'],
    labels=df['Team'],
    colors=teamColours,
    startangle=90,
    autopct='%1.1f%%'
)
ax.set_title("MoneyNotPassion League Titles")
ax.axis('equal')

st.title("Statistics")
st.pyplot(fig)
