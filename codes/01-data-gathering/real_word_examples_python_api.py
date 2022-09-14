import json
import tweepy
import openpyxl

#generate excel
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'correct news'

# load key
consumer_key = "OA4CTZkyLwMOg08PlFt0goCNC"
consumer_secret = "8k59TeAGeqlHXjf4wjOjrKLYXpEvutuRgDjLxVxm5R7uC5wB0q"
access_token = "1177285260242874368-QoMZGUj2TsbkXyPQ5o0pu5iFrFT72q"
access_token_secret = "6JWjo6Ro4RmqIBFLjOop9QW1FCgHZltRTz8EIsj9UiMOE"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAISeXgEAAAAANwEgP0gtkLS%2Bjv9qCa3pIB3o1xs%3D98KYFXJI2DYHslg3StyrI2h9aB0w8PYq8iJyGS6Vdwsrhgkt7r"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

# download information
tweets=api.user_timeline(user_id=1367531,count=50,tweet_mode='extended')
for tweet in tweets:
    tweet=tweet._json['full_text']
    sheet.append(['Fox News',tweet])

wb.save(r"D:\501\correct information.xlsx")

