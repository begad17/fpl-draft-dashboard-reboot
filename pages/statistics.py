import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.title("Statistics & League History")

# Carousel Slide Selector
slide = st.radio("Select Statistic View:", ["League Titles", "Manager of the Month"])

# League Titles Pie Chart
if slide == "League Titles":
    leagueWins = {'Team':['Jordan (1)','Begad (1)','Moe (1)'], 'Championships':[1,1,1]}
    df = pd.DataFrame(leagueWins)
    teamColours = ['#f40206','#0560b5','#ce0000']

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

    st.pyplot(fig)

# MVP Bar Chart
elif slide == "Manager of the Month":
    mvp_counts = {
        "Moe": 3,
        "Connor": 3,
        "Michael": 1,
        "Fawzi": 2,
        "Begad": 1
    }

    managers = list(mvp_counts.keys())
    counts = list(mvp_counts.values())

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(managers, counts, color='skyblue', edgecolor='black')

    ax.set_title("Manager of the Month Awards")
    ax.set_xlabel("Manager")
    ax.set_ylabel("Number of Times Won")

    for i, bar in enumerate(bars):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.1,
            str(counts[i]),
            ha='center',
            va='bottom'
        )

    fig.tight_layout()
    st.pyplot(fig)

