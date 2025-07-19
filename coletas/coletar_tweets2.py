import tweepy 
import re 
import unicodedata
import pandas as pd

#acesso à API do Twitter
client = tweepy.Client(
    bearer_token='AAAAAAAAAAAAAAAAAAAAAN2S3AEAAAAA5%2FphMWCesRx6KKzdmhizG6wdfgg%3DPVmyjaLFjMMwER2VYPlPlXZkY2RyyIiq0bAplbS5TdB1Si0VLM',
    wait_on_rate_limit=True
)

#Parâmetros da consulta
tema = "apostas manipuladas OR bets"
query = f'({tema}) lang:pt -is:retweet'

# Busca
tweets = client.search_recent_tweets(
    query=query,
    tweet_fields=["created_at", "author_id", "lang"],
    max_results=59
)

#Verificação se há resultados
info = [t.text for t in tweets.data] if tweets.data else []
print(info)

#limpeza de texto
def limpar_tweet(tweet):
    tweet = re.sub(r'https?://\S+', '', tweet)
    tweet = re.sub(r'#\w+', '', tweet)
    tweet = re.sub(r'@\w+', '', tweet)
    tweet = ''.join(c for c in tweet if unicodedata.category(c)[0] != 'So')
    tweet = re.sub(r'\s+', ' ', tweet)
    tweet = tweet.strip()
    return tweet

#Aplicação 
dados_filtrados = [limpar_tweet(t) for t in info]
print(dados_filtrados)

#Criação do DataFrame
df = pd.DataFrame({'Descrição': dados_filtrados})
print(df.head())

#Salvando os arquivos
df.to_csv('tweets_bets.csv', sep= ',')
