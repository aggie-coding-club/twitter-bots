import tweepy
import time as time
import Access_Keys as keys
import huffman as huff
import Decoder as decode
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
myFile = open("used_IDs.txt")
text = myFile.read()
used_IDs = []
used_IDs = text.split(",")
myFile.close()
print(len("@bot90861498 Key: [[' ', '00'], ['m', '010'], ['s', '011'], [')', '1000'], [':', '1001'], ['e', '101'], ['p', '1100"))
while(True):
   mentions = api.mentions_timeline()
   
   for mention in mentions:
      statusID = mention.id
      if(not(mention.id_str in used_IDs) and str(mention.user.screen_name) != "bot90861498" and ("decode" in mention.text.lower())):
         try:
            status = api.get_status(statusID, tweet_mode = "extended")
            text = status.full_text.lower()
            output = decode.decode(text)
            api.update_status(status = output, in_reply_to_status_id = mention.id)
         except:
            api.update_status(status = "I wasn't able to decode your message :(", in_reply_to_status_id = mention.id);
         used_IDs.append(mention.id_str)
         myFile = open("used_IDs.txt", 'w')
         for used_ID in used_IDs:
            if(used_ID != ""):
               myFile.write(used_ID + ",")
         myFile.close()
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
         myFile = open("used_IDs.txt", 'w')
         for used_ID in used_IDs:
            if(used_ID != ""):
               myFile.write(used_ID + ",")
         myFile.close()
         time.sleep(15)
      if(not(mention.id_str in used_IDs) and str(mention.user.screen_name) != "bot90861498" and ("time" in mention.text)):
         text = "@" + str(mention.user.screen_name) + " Hello! it is " + str(time.gmtime().tm_mon) + "/" + str(time.gmtime().tm_mday) + "/" + str(time.gmtime().tm_year) + " " + str(time.gmtime().tm_hour) + ":" + str(time.gmtime().tm_min) + ":" + str(time.gmtime().tm_sec) + " UTC"
         api.update_status(status = text, in_reply_to_status_id = mention.id)
         used_IDs.append(mention.id_str)
         myFile = open("used_IDs.txt", 'w')
         for used_ID in used_IDs:
            if(used_ID != ""):
               myFile.write(used_ID + ",")
         myFile.close()
         time.sleep(15)
   time.sleep(60)

