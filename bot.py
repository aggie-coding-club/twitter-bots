import tweepy
import time as time

# import in the other functions
import interaction
import method_keywords
import method_quiz
import method_random
import keys
consumer_key = keys.CONSUMER_KEY
consumer_secret = keys.CONSUMER_SECRET
access_token = keys.ACCESS_TOKEN
access_token_secret = keys.ACCESS_TOKEN_SECRET

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)
API = tweepy.API(auth)
BOT_LIST = ["textmanipulator", "bot90861498", "sheevsdemocracy", "Nitsuabot", "twt_stanley"]

#returns a list of status objects representing all of the mentions in the current timeline
def get_mentions():
    mentions = []
    for mention in API.mentions_timeline():
        mentions.append(mention)
    return mentions

#returns a list of strings representing the ids of mentions in the current timeline
def get_mention_ids():
    mentions = []
    for mention in API.mentions_timeline():
        mentions.append(mention.id_str)
    return mentions

#returns a list of status objects representing the newest mentions
def new_mentions(old_mention_ids, current_mentions):
    new_mentions = []
    for mention in current_mentions:
        if(not mention.id_str in old_mentions):
            new_mentions.append(mention)
    return new_mentions
#returns the text for the quiz
def quiz_text():
    return ""

#returns point value based on user's response
def add_points(user_answer):
    return 0

#returns username of bot based on points
def decide_bot(points):
    return ""

#returns the text of the bot's response, uses add_points and decide_bot
def response(user_answer):
    return ""

def main():
    old_mention_ids = get_mention_ids()
    while(True):
        current_mentions = get_mentions()
        newest_mentions = new_mentions(old_mention_ids, current_mentions)
        for mention in new_mentions:
            recommended = method_keywords.keywords(mention)
            text = "@" + mention.user.screen_name 
            if(recommended != ""):
                text += " We recommend these bots: " + recommended
            else:
                text += " Here is a randomly recommended bot: " + method_random.random()
            API.update_status(text = text, in_reply_to_status_id = mention.id)
        time.sleep(60)

main()