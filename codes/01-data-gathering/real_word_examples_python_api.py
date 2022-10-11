import json
import tweepy
import pandas as pd

# load key
consumer_key = "OA4CTZkyLwMOg08PlFt0goCNC"
consumer_secret = "8k59TeAGeqlHXjf4wjOjrKLYXpEvutuRgDjLxVxm5R7uC5wB0q"
access_token = "1177285260242874368-QoMZGUj2TsbkXyPQ5o0pu5iFrFT72q"
access_token_secret = "6JWjo6Ro4RmqIBFLjOop9QW1FCgHZltRTz8EIsj9UiMOE"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAISeXgEAAAAANwEgP0gtkLS%2Bjv9qCa3pIB3o1xs%3D98KYFXJI2DYHslg3StyrI2h9aB0w8PYq8iJyGS6Vdwsrhgkt7r"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#write a function to collect some news and related statistical number
def truth(userid):
    tweets=api.user_timeline(user_id=userid,count=50,tweet_mode='extended') 
    text=[]
    location=[]
    friends_count=[]
    followers_count=[]
    screen_name=[]
    retweet_count=[]
    favorite_count=[]
    description=[]
#store what we need in a list 
    for tweet in tweets:
        text.append(tweet._json['full_text'])
        location.append(tweet._json["user"]["location"])
        friends_count.append(tweet._json["user"]["friends_count"])
        followers_count.append(tweet._json["user"]["followers_count"])
        screen_name.append(tweet._json["user"]["screen_name"])
        description.append(tweet._json["user"]["description"])
        retweet_count.append(tweet._json['retweet_count'])
        favorite_count.append(tweet._json['favorite_count'])
#transform the list into dictionary
    dic={"text":text,"location":location,"friends_count":friends_count,"followers_count":followers_count,"screen_name":screen_name,"retweet_count":retweet_count,"favorite_count":favorite_count,"description":description}
    df=pd.DataFrame(dic)
    return(df)
df=truth(1367531)

for i in[5402612,15012486,1120655269,380648579,86141342,7309052,15679641,10433782,6577642]:
    df=pd.concat([df, truth(i)])

df.to_csv(r"C:\Windows\System32\anly-501-project-FlynnFlag\data\00-raw-data\truth.csv")

