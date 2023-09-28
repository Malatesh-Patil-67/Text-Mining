import tweepy

# Set your Twitter API credentials
consumer_key = 'hxul1DqPOdjK30XUyh7h7XxLL'
consumer_secret = 'W6R9HbxNZtxn0ujPD6qBIALvAQFbcUsXmJyjuTmIDC1OCdni9W'
access_token = '1698665673075965952-S0YSfjdSfdHFHVhNDZCOAWFEdyMhby'
access_token_secret = 'dGJcVCyps0fzaepcMMAkemTN0ry3PP0rPJsNwNTRCkDhW'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.Client(auth, wait_on_rate_limit=True)


# Define search parameters
search_query = 'Bundesliga23'  # Replace with your query
num_tweets = 100  # Adjust the number of tweets to fetch

# Extract tweets
tweets = []

for tweet in api.search_recent_tweets(query=search_query, max_results=num_tweets, lang='en'):
    tweets.append(tweet.text)

# Print the first few tweets
for i, tweet in enumerate(tweets):
    print(f'Tweet {i + 1}: {tweet}')



