import bot
import tweepy

# give method options
def giveMethodOptions():
    message = "Reply with a recommendation option:\n [1] Random\n [2] Quiz\n [3] Keywords"
    bot.API.update_status(message)

# check options
# def checkForMethod(userReply):
#     for char in userReply:
#         if char == "1":
           
#         else if char == "2":
