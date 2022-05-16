import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import json,urllib.request
import streamlit as st
import plotly.express as px





try:
    nlp = spacy.load("en_core_web_md")
except: # If not present, we download
    spacy.cli.download("en_core_web_md")
    nlp = spacy.load("en_core_web_md")

nlp.add_pipe("spacytextblob")

data = urllib.request.urlopen("https://globaltwittertrends.com/peri.json").read()
output = json.loads(data)
name = []
volume = []
ee = []
ee2 = ['positive','negative']
text = []


x = 0

while(x < len(output)):
	doc = nlp(output[x][2])
	yy = doc._.subjectivity
	print(output[x][2])
	x= x +1
	volume.append(yy)
	if(yy > 0.49):
		ee.append("positive")
	else:
		ee.append("negative")

 
# Random Data
random_x = volume
names = ee
 
fig = px.pie(values=random_x, names=names,title='Ukraine War')


st.plotly_chart(fig)

		
