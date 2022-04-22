import random
import bot

# pick random bot
def pickRandomBot():
    randomBot = random.randrange(0,len(bot.BOT_LIST)-1)
    return bot.BOTLIST[randomBot]

