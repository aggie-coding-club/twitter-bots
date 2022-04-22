import bot
import tweepy

# send first prompt
def sendFirstPrompt(user_id):
    text = "QUIZ TIME\n\nLet's begin your quiz to see what bot you should follow!"
    bot.API.send_direct_message(user_id, text)

    text = "1) Do you lik"
    bot.API.send_direct_message(user_id, text)
