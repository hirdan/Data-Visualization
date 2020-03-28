# installing  twitter module
#!pip  install tweepy
import  tweepy

#  defining variables
#  consumer key 
consumer_key=""
consumer_sec=""
# access details
access_key = access_sec=

# lets  connect  at  first step auth by using consumer  access details 
#dir(tweepy)
first_auth=tweepy.OAuthHandler(consumer_key,consumer_sec)

#  now setting  second level of auth
first_auth.set_access_token(access_key,access_sec)

#  pointing  auth to datastore
storage_api_connect=tweepy.API(first_auth,timeout=10)  #  now after this step we can browse / search data from tweetes

# now  searching  data  as req and waiting  for reply  
#  first  method 
#tweet_data=storage_api_connect.search('corona',count=25)

#  second method
from textblob  import  TextBlob   #  automated way of sentiment analysis 
search_data=["corona"]  #  search list
list_of_tweets=[]   #  tweet data store

if  len(search_data) >= 1 : 
  for  i  in  tweepy.Cursor(storage_api_connect.search,q=search_data[0]+"  -filter:retweets",lang='en',result_type='recent').items(100):
    analyse=TextBlob(i.text)
    print(analyse.sentiment.polarity)
    #print(i.text)

#print(list_of_tweets)

#  use for loop
#for  data   in   tweet_data:
# print(data.text)
