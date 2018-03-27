import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import csv
import sys
import datetime as dt
import matplotlib.pyplot as plt
 
class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = '*********************'
        consumer_secret = '***********************'
        access_token = '******************************'
        access_token_secret = '***************************'
 
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def write_tweet(self,tweet,sentiment):
        
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow([tweet, sentiment])
        
 
    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
        
        try:
            # call twitter api to fetch tweets
            td = dt.datetime.now() - dt.timedelta(days=9)
            tweet_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
            fetched_tweets = self.api.search(q = query, count = count, until=tweet_date)
            
            #Open CSV file to write tweets
            csvFile = open('C:\\Users\\mmajgaon.ORADEV\\Desktop\\NLP\\GST\\tweet_data.csv', 'a')
            csvWriter = csv.writer(csvFile)
            
            # parsing tweets one by one
            for tweet in fetched_tweets:

                #Write the tweet in CSV file
                tw = self.clean_tweet(tweet.text)
		if tweet.lang == "en":
                    csvWriter.writerow([tw.encode('utf-8')])

                # empty dictionary to store required params of a tweet
                parsed_tweet = {}
 
                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
 
                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
            csvFile.close()
 
            # return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
		
def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    #Take into account all the variants of GST phrase while tweeting
    search_phrases= ['GST','gst','Goods and Services Tax']
    for search_phrase in search_phrases:
        tweets = api.get_tweets(query = search_phrase, count = 20000)
        
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    positive = 100*len(ptweets)/len(tweets)
    print("Positive tweets percentage: {} %".format(positive))
    
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    negative = 100*len(ntweets)/len(tweets)
    print("Negative tweets percentage: {} %".format(negative))

    #Picking neutral tweets
    otweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    
    # percentage of neutral tweets
    neutral = 100*len(otweets)/len(tweets)
    print("Neutral tweets percentage: {} % ".format(neutral))
          
    # Store Positive Tweets
    pFile = open('C:\\Users\\mmajgaon.ORADEV\\Desktop\\NLP\\GST\\postive_tweets.csv', 'a')
    csvWriter1 = csv.writer(pFile) 
    for tweet in ptweets:
        csvWriter1.writerow([tweet['text'].encode('utf-8')])
    pFile.close()
          
    # Store negative
    nFile = open('C:\\Users\\mmajgaon.ORADEV\\Desktop\\NLP\\GST\\negative_tweets.csv', 'a')
    csvWriter2 = csv.writer(nFile)
    for tweet in ntweets:
        csvWriter2.writerow([tweet['text'].encode('utf-8')])
    nFile.close()

    # Store neutral tweets
    oFile = open('C:\\Users\\mmajgaon.ORADEV\\Desktop\\NLP\\GST\\neutral_tweets.csv', 'a')
    csvWriter3 = csv.writer(oFile)    
    for tweet in otweets:
          csvWriter3.writerow([tweet['text'].encode('utf-8')])
    oFile.close()

    #Plot the pie chart about the analysis
    labels = 'Positive reviews', 'Negative Reviews', 'Neutral reviews'
    sizes = [positive, negative, neutral]
    colors = ['gold', 'green', 'red']
    explode = (0.1, 0, 0)

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
 
    plt.axis('equal')
    plt.show()
if __name__ == "__main__":
    # calling main function
    main()

