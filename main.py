from coletas import coletar_tweets2
from coletas import coletar_web
from coletas import analise_nlp
from coletas import analise_sentimental

def main():
    print("🚀 Iniciando pipeline de análise NLP sobre apostas...\n")

    # Etapa 1: Coleta de Dados
    print("📥 Coletando tweets...")
    coletar_tweets2()

    print("\n📰 Coletando notícias...")
    coletar_web()

    # Etapa 2: Análise Linguística
    print("\n🔎 Realizando análise linguística...")
    analise_nlp()

    # Etapa 3: Análise de Sentimento
    print("\n❤️ Classificando sentimentos...")
    analise_sentimental()

    print("\n✅ Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    main()
