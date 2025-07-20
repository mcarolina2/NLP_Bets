import pandas as pd
from textblob import TextBlob
import os

def classificar_sentimento(texto):
    if pd.isna(texto):
        return 'neutro'
    analise = TextBlob(str(texto))
    polaridade = analise.sentiment.polarity
    if polaridade > 0:
        return 'positivo'
    elif polaridade < 0:
        return 'negativo'
    else:
        return 'neutro'

def analisar_arquivo(nome_arquivo):
    print(f"\n📁 Verificando arquivo: {nome_arquivo}")
    if not os.path.exists(nome_arquivo):
        print(f"🚫 Arquivo '{nome_arquivo}' não encontrado.")
        return

    df = pd.read_csv(nome_arquivo)
    print(f"✅ Arquivo carregado com {len(df)} linhas.")

    coluna_texto = 'text' if 'text' in df.columns else df.columns[0]
    print(f"📝 Aplicando análise na coluna: {coluna_texto}")

    df['sentimento'] = df[coluna_texto].apply(classificar_sentimento)

    nome_saida = nome_arquivo.replace('.csv', '_com_sentimento.csv')
    df.to_csv(nome_saida, index=False)
    print(f"💾 Resultado salvo em: {nome_saida}")

# Executa para ambos os arquivos
analisar_arquivo('coletas/tweets_bets.csv')
analisar_arquivo('coletas/noticias_bets.csv')
