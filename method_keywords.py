import tweepy
#returns list of bots to recommend based on keywords
def keywords(status, api):
    output = ""
    keywords = {"democracy": "@sheevsdemocracy", "compress" : "@bot90861498", "compression"  : "@bot90861498", "stanley" : "@twt_stanley", "flat" : "@twt_stanley", "manipulate" : "@textmanipulator"}
    text = status.text
    for key in keywords:
        if(key in text and (not(keywords[key] in output))):
            output += keywords[key] + ", "
    if(len(output) != 0):
        output = output[:-2]
    return output