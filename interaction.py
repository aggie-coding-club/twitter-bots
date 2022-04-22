import bot
import tweepy

# give method options
def giveMethodOptions():
    message = "Reply with a recommendation option:\n [1] Random\n [2] Quiz\n [3] Keywords"
    bot.API.update_status(message)

# check options
# def checkForOption(userReply):
    