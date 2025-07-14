import tweepy

bearer_token = "coloque seu token da api aqui" 

client = tweepy.Client(bearer_token = bearer_token)

query = "bets -is:retweet lang:pt"

response = client.search_recent_tweets(
    query=query,
    tweet_fields=["created_at", "author_id", "text"],
    expansions=["author_id"],
    user_fields=["username", "name"],
    max_results=30
)

if response.data:
  for tweet in response.data:
    print(f"{tweet.created_at} | {tweet.text} | {tweet.author_id}\n")
else:
  print("Nenhum tweet encontrado.")
