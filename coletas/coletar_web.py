import requests
import pandas as pd

API_KEY = '7997e5fe8f584ffc8ee1a3468551b871'  # minha chave
query = 'apostas manipuladas OR CPI das bets'

url = f'https://newsapi.org/v2/everything?q={query}&language=pt&sortBy=publishedAt&apiKey={API_KEY}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    artigos = data['articles']

    noticias = []
    for artigo in artigos:
        noticias.append({
            'Título': artigo['title'],
            'Fonte': artigo['source']['name'],
            'Publicado em': artigo['publishedAt'],
            'Descrição': artigo['description'],
            'URL': artigo['url']
        })

    df = pd.DataFrame(noticias)
    print(df)
    df.to_csv('noticias_bets.csv', index=False)
else:
    print('Erro:', response.status_code, response.text)
