import tweepy

bearer_token = "AAAAAAAAAAAAAAAAAAAAALYV3AEAAAAActXV3SxScK8Pfo9tTd9kfkb1rQQ%3DaMpNn1Iu0EJxr0yMY1qk6Euot5p2gFC41FHYcrZRn8cz1jrHiq" 

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