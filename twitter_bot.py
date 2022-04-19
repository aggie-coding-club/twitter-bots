import tweepy
import time as time
import huffman as huff
import Decoder as decode
from os import environ

consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']
auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
#api.update_status("Hello world!")

used_IDs = []
for mention in api.mentions_timeline():
   used_IDs.append(mention.id_str)
while(True):
   mentions = api.mentions_timeline()
   
   for mention in mentions:
      statusID = mention.id
      if(not(mention.id_str in used_IDs) and str(mention.user.screen_name) != "bot90861498" and ("decode" in mention.text.lower())):
         screen_name = "@" + str(mention.user.screen_name) + " ";
         try:
            status = api.get_status(statusID, tweet_mode = "extended")
            text = status.full_text.lower()
            output = screen_name + decode.decode(text)
            api.update_status(status = output, in_reply_to_status_id = mention.id)
         except:
            api.update_status(status = screen_name + "I wasn't able to decode your message :(", in_reply_to_status_id = mention.id);
         used_IDs.append(mention.id_str)
        
         time.sleep(15)
      if(not(mention.id_str in used_IDs) and str(mention.user.screen_name) != "bot90861498" and ("compress" in mention.text.lower())):
         status = api.get_status(statusID, tweet_mode = "extended")
         text = status.full_text.lower()
         text = text[12:]
         output = huff.huffman(text)
         i = 0;
         curr_message = "@" + str(mention.user.screen_name) + " "
         message_count = 0;
         while(i < len(output)):
            curr_message += output[i];
            if(len(curr_message) == 279):
               tweets = api.user_timeline()
               if(message_count == 0):
                  api.update_status(status = curr_message, in_reply_to_status_id = mention.id)
               else:
                  api.update_status(status = curr_message, in_reply_to_status_id = tweets[0].id)
               message_count += 1
               curr_message = "@" + str(tweets[0].user.screen_name) + " "
            i += 1
         if(message_count == 0):
            api.update_status(status = curr_message, in_reply_to_status_id = mention.id)
         else:
            tweets = api.user_timeline()
            api.update_status(status = curr_message, in_reply_to_status_id = tweets[0].id)
         used_IDs.append(mention.id_str)
         
         time.sleep(15)
      if(not(mention.id_str in used_IDs) and str(mention.user.screen_name) != "bot90861498" and ("time" in mention.text)):
         text = "@" + str(mention.user.screen_name) + " Hello! it is " + str(time.gmtime().tm_mon) + "/" + str(time.gmtime().tm_mday) + "/" + str(time.gmtime().tm_year) + " " + str(time.gmtime().tm_hour) + ":" + str(time.gmtime().tm_min) + ":" + str(time.gmtime().tm_sec) + " UTC"
         api.update_status(status = text, in_reply_to_status_id = mention.id)
         used_IDs.append(mention.id_str)
         
         
         time.sleep(15)
   time.sleep(60)

