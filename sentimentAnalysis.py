#this thing does wonders i did not build the model 
#check readme file for more info 

from transformers import pipeline

import pandas as pd

# Load pipeline
#basically i steal someones model here and ploop
sentiment_pipeline = pipeline("sentiment-analysis")

#uses scraped data from the excel sheet
data = pd.read_excel("copy path directory here")

#mapping lol idk if its counted as mapping
good = 0
bad = 0

#im sure you know what this does, in fact you can extract and do more stuff with the results using your creativity
for index, row in data.iterrows():
    text = row["Message"]  
    result = sentiment_pipeline(text)
    label = result[0]['label']
    if label == 'POSITIVE':
        good += 1
    elif label == 'NEGATIVE':
        bad += 1
    print(result)

#its more of a correlation whether the 2 of yall have a great connection
print("how much they like you:", good)
print("how much they hateeee you:", bad)
