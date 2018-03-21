# GSTTweets
Python Script to get the GST Tweets and do sentiment analysis on it

To Run this script we will require Python 3 and some python packages installed.

1) Tweepy: Tweepy is the python client for the official Twitter API.
    pip install tweepy
 
2) TextBlob: Textblob is the python library for processing textual data.
   pip install textblob
   
3) NLTK corpora:Sample corpora used for training the dataset
   python -m textblob.download_corpora
 
4) MatPlotLib: Used to plot the analysis (We use pie chart to plot the analysis here)
   python -mpip install -U matplotlib
   

In this python code we extarct the tweets on GST for last 9 days and analyse them for which tweets are positive, negative or neutral.

This sentiment analysis is done by traing the extracted tweets on the NLTK corpora.

The tweets are seperated based on their sentiments and stored in different CSV files

1) tweet_data.csv - stores are the retrieved tweets
2) positive_tweets.csv - stores all the positive tweets
3) negative_tweets.csv - stores all the negative tweets.
4) neutral_teets.csv - stores all the neutral tweets.

These tweet seperation based on sentiments is will be used in training sets later on.

For now simple Naive Bayes Classfier is used for Sentiment Classification.
