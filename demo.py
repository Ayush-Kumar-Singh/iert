import snscrape.modules.twitter as sntwitter
import pandas as pd
import json
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px
from datetime import datetime

output = pd.read_pickle("https://howmany.site/ayush.pkl")
st.write(output)
month = 1
xaxis = []
yaxis = []
posaxis = []
nueaxis = []
def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
        fig.data[i].name = new_name

while(month < 13):
  
  New_df = output.loc[output["Month"] ==  month]
  New_df2 = New_df.loc[New_df["Sentiment"] == "Negative"]
  New_df3 = New_df.loc[New_df["Sentiment"] == "Positive"]
  New_df4 = New_df.loc[New_df["Sentiment"] == "Neutral"]

  if(len(New_df2) > 0):
    
    percentage2 = len(New_df2)/len(output)
    percentage3 = percentage2 * 100 
    yaxis.append(percentage3)
    pos = len(New_df3)/len(output)
    pos2 = pos * 100
    posaxis.append(pos2)

    nue = len(New_df4)/len(output)
    nue2 = nue * 100
    nueaxis.append(nue2)
  else:
    yaxis.append(0)

  
  month = month + 1


xaxis = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
st.balloons()

fig = px.line( x=xaxis, y=[yaxis,posaxis,nueaxis], title='Sentiment By Month', markers= True)
fig.update_layout(
    title="Sentimental Analysis By Month",
    xaxis_title="Month",
    yaxis_title="Sentiment",

    legend_title="Sentiment By Month",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)
custom_legend_name(["Negative Sentiment", "Positive Sentiment", "Neutral Sentiment"])
st.plotly_chart(fig)
st.write(xaxis)
st.write("Negative",yaxis)


st.write("Positive",posaxis)
st.write("Neutral",posaxis)

st.write("Most Negative Tweet")
New_df = output.loc[output["Negative"] ==  output["Negative"].max()]
st.write(New_df)
st.write("Most Positive Tweet")
New_df = output.loc[output["Positive"] ==  output["Positive"].max()]
st.write(New_df)
st.write("Most Neutral Tweet")
New_df = output.loc[output["Neutral"] ==  output["Neutral"].max()]
st.write(New_df)
