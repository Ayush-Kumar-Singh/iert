def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
        fig.data[i].name = new_name
import snscrape.modules.twitter as sntwitter
import pandas as pd
import json
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px
from datetime import datetime



analyzer = SentimentIntensityAnalyzer()

tweets_list1 = []
tcontent = []
tusername = []
tid = []
tdate = []
volume = []
ee = []
volume = []
ee = []
# Random Data



title = st.text_input('Find Sentiment', 'Ukraine War')
heading = "Sentimental Analysis Of " + title + " Tweets"
option = st.selectbox(
     'How would tweets do you want to analyze?',
     (100, 1000, 10000, 100000, 1000000))
dev = int(option/100)

my_bar = st.progress(0)

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(title +' since:2021-01-01 until:2021-12-31').get_items()): #declare a username 
    if i>option:
        break
    st.write(tweet)
    tcontent.append(tweet.content)
    tusername.append(tweet.user.username)
    tid.append(tweet.id)
    d = datetime.strptime(str(tweet.date), '%Y-%m-%d %H:%M:%S+00:00')
    tdate.append(d.day)
    
    vs = analyzer.polarity_scores(tweet.content)
    pos = vs['pos'] * 100
    neg = vs['neg'] * 100
    neu = vs['neu'] * 100
    
    volume.append(1)
    if vs['compound'] >= 0.05 :
        
        ccc = "Positive"
        
 
    elif vs['compound'] <= - 0.05 :
        
        ccc = "Negative"
        
    else :
        
        ccc = "Neutral"
        
    ee.append(ccc)
    if(i % dev == 0):
        my_bar.progress(int(i/dev))
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username, ccc, d.month,pos, neg, neu])


my_bar.empty()
random_x = volume
names = ee
 
fig = px.pie(values=random_x, names=names,title=heading)

st.plotly_chart(fig)



    
# Creating a dataframe from the tweets list above 
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Sentiment', 'Month', 'Positive', 'Negative', 'Neutral'])

tweets_df1.to_pickle("ayush.pkl")
output = pd.read_pickle("ayush.pkl")
st.write(output)
month = 1

yaxis = []
posaxis = []
nueaxis = []


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
    posaxis.append(0)
    nueaxis.append(0)

  
  month = month + 1


xaxis = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
st.balloons()
st.write(len(xaxis),len(yaxis),len(posaxis),len(nueaxis))

fig = px.line( x=xaxis, y=[yaxis,posaxis,nueaxis], title=heading, markers= True)
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
