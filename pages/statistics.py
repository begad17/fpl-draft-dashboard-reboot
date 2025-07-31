import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

leagueWins = {'Team':['Jordan (1)','Begad (1)', 'Moe (1)'],
             'Championships':[1,1,1]}

df = pd.DataFrame(leagueWins, columns=['Team','Championships'])

plt.pie(df['Championships'])

#This next line just makes the plot look a little cleaner in this notebook
plt.tight_layout()

#Create a list of the colours used for the teams, in order.
teamColours=['#f40206','#0560b5','#ce0000','#1125ff','#28cdff','#091ebc']

plt.pie(df['Championships'],
        #Data labels are the team names in the dataFrame
       labels = df['Team'],
        #Assign our colours list
       colors = teamColours,
        #Give a tidier angle to ur first data angle
        startangle = 90
       )

#Add a title
plt.title("MoneyNotPassion League Titles")
plt.tight_layout()

plt.show()
