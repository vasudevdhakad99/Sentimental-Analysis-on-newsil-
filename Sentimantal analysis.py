# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:05:39 2023

@author: star26
"""

# Import necessary libraries
from textblob import TextBlob
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Sample list of news article URLs
article_urls = [
    "https://www.example.com/article1",
    "https://www.example.com/article2",
    "https://timesofindia.indiatimes.com/city/agartala/posco-court-in-tripura-sentences-two-to-death-for-rape-murder-of-minor-girl/articleshow/104156123.cms",
    "https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/news"
]

# Function to fetch the content of a URL
def get_article_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')  # Assuming the article content is in <p> tags
        content = ' '.join([p.get_text() for p in paragraphs])
        return content
    except Exception as e:
        print(f"Error fetching content from {url}: {str(e)}")
        return None

# Sample crude oil news headlines with corresponding URLs
news_data = [
    {"headline": "Oil prices surge as OPEC agrees to production cuts", "url": "https://www.example.com/article1"},
    {"headline": "Environmental concerns lead to a drop in crude oil prices", "url": "https://www.example.com/article2"},
    {"headline": "POSCO court in Tripura sentences two to death for rape, murder of minor girl", "url": "https://timesofindia.indiatimes.com/city/agartala/posco-court-in-tripura-sentences-two-to-death-for-rape-murder-of-minor-girl/articleshow/104156123.cms"},
    {"headline": "Breaking news about Bollywood celebrities to entertaining gossip and all the updates about film releases - this is your one stop destination to all things movies. From who is making their big debut in Bollywood to which movie is setting the box office on fire and new film announcements ", "url":"https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/news"},
]

# Create a DataFrame to store the news data
df = pd.DataFrame(news_data)

# Function to perform sentiment analysis using TextBlob
def perform_sentiment_analysis(url):
    content = get_article_content(url)
    if content:
        analysis = TextBlob(content)
        if analysis.sentiment.polarity > 0:
            return "Positive"
        elif analysis.sentiment.polarity < 0:
            return "Negative"
        else:
            return "Neutral"
    else:
        return "Error"

# Apply sentiment analysis to the URLs and add the results to the DataFrame
df['sentiment'] = df['url'].apply(perform_sentiment_analysis)

# Print the DataFrame with sentiment analysis results
print(df)
