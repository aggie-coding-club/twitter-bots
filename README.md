# Twitter Bots

Making our lil twitter bots to do their lil bot thing. ACC Project for Spring Semester 2022.

---

## Getting Started

### 0) Make a twitter account.

*You don't have to do this step if you already have a twitter account. You can also do this step if you want to have a different account for your bot.*

1. Go to <https://twitter.com/>
2. Click one of the sign up options
3. Make an account (either with phone or email)
  - If you don't want to make a new email you can make a new one that still sends to your normal inbox using and "+" to add an extension. So if your normal email was "bob@gmail.com" you can make a new email with "bob+code@gmail.com"
  - Twitter bots occassionally get restricted for tweeting too often, so if you're worried that this may happen, add a phone number so that you can easily unrestrict it. 

**At this point, you can use Cheap Bots Done Quick!, Tweepy or both. For our project, we're going to use Cheap Bots Done Quick! to learn some basics and then Tweepy to create a larger project.**

---

### Cheap Bots Done Quick!

*The bot will automatically begin tweeting from the account that you're signed into*

1. Go to <https://cheapbotsdonequick.com/> while being signed into twitter in the same browser.
  -  make sure your twitter account is not privated
2. Edit the JSON file as you see fit.
  - Cheap Bots Done Quick! will automatically randomly generate tweets from the options listed in the JSON file.
3. Change the settings for how often your bot should tweet, whether it should reply to people or not.

### Tweepy

##### 1) Make a twitter developer account.

1. Go to <https://developer.twitter.com/en>
2. Click "Sign Up" and fill out the information requested.
  - This automatically gets you access to Twitter API v2. This is Twitter's newer API and is more limited in some ways compared to Twitter API v1.1. Check <https://developer.twitter.com/en/docs/twitter-api/v1> to see if it fits the needs of the bot you want to make.
  - [OPTIONAL] Apply for greater access. Navigate to the Twitter Developer Dashboard at <https://developer.twitter.com/en/portal/dashboard> and click the button to "Apply for Elevated Access" which will get you access to Twitter API v1.1. You will need to fill out a more detailed form and may have to send additional details via email.
3. Create a Project.
4. Generate Keys and Tokens.

##### 2) Install Tweepy

Install tweepy via Powershell, Terminal, or Bash:

``pip install tweepy``

*Futher installation guides found here: <https://docs.tweepy.org/en/stable/install.html>*

