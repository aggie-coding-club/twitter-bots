import config
import tweepy
import googletrans
import random

auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET) 

client = tweepy.Client(consumer_key=config.API_KEY,
                       consumer_secret=config.API_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_SECRET)

msg = "hello world"
translator = googletrans.Translator()
languages = [lang for lang in googletrans.LANGUAGES] 
for i in range(0, 10):
    lang = languages[random.randrange(0, len(languages))]
    msg = translator.translate(msg, dest=lang).text
msg = translator.translate(msg, dest="en").text
response = client.create_tweet(text=msg)
