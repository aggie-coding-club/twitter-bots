import tweepy
import time as time
import Access_Keys as keys
consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret
auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
#api.update_status("Hello world!")
while(True):
   mentions = api.mentions_timeline()
   myFile = open("used_IDs.txt")
   text = myFile.read()
   used_IDs = []
   used_IDs = text.split(",")
   myFile.close()
   for mention in mentions:
      if(not(mention.id_str in used_IDs)):
         text = "@" + str(mention.user.screen_name) + " Hello! it is " + str(time.gmtime().tm_mon) + "/" + str(time.gmtime().tm_mday) + "/" + str(time.gmtime().tm_year) + " " + str(time.gmtime().tm_hour) + ":" + str(time.gmtime().tm_min) + ":" + str(time.gmtime().tm_sec) + " UTC"
         api.update_status(status = text, in_reply_to_status_id = mention.id)
         used_IDs.append(mention.id_str)
         myFile = open("used_IDs.txt", 'w')
         for used_ID in used_IDs:
            if(used_ID != ""):
               myFile.write(used_ID + ",")
         myFile.close()
         time.sleep(15)

