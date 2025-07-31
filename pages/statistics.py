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

# MVP stats
mvp_counts = {
    "Moe": 3,
    "Connor": 3,
    "Michael": 1,
    "Fawzi": 2,
    "Begad": 1
}

# Data for the chart
managers = list(mvp_counts.keys())
counts = list(mvp_counts.values())

# Create bar chart using Matplotlib
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(managers, counts, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title("Manager of the Month Awards")
ax.set_xlabel("Manager")
ax.set_ylabel("Number of Times Won")

# Add value labels on top of bars
for i, bar in enumerate(bars):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.1,
        str(counts[i]),
        ha='center',
        va='bottom'
    )

fig.tight_layout()

# Show the chart in Streamlit
st.pyplot(fig)
