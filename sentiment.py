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


for x in range(len(output['statuses'])):
	if(output['statuses'][x]['text'] is not None):
		
		doc = nlp(output['statuses'][x]['text'])
		ayush = output['statuses'][x]['user']['name']
		yy = doc._.subjectivity
		if(yy > 0):
			name.append(ayush)
			volume.append(yy)
			text.append(output['statuses'][x]['text'])
			if(yy > 0.49):
				ee.append("positive")
			else:
				ee.append("negative")

 
# Random Data
random_x = volume
names = ee
 
fig = px.pie(values=random_x, names=names,title='Sentimental Analysis Of Tweets')


st.plotly_chart(fig)

st.write(name)
st.write(text)

		
