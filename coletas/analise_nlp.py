import pandas as pd
import spacy
import os
import re

# modelo de português do spaCy
nlp = spacy.load("pt_core_news_sm")

# caminhos de entrada e saída
input_files = ["noticias_bets.csv", "tweets_bets.csv"]
output_folder = "resultados"
os.makedirs(output_folder, exist_ok=True)

regex_filtro = r"\b(apostas|jogo|bets)\b"

print("Iniciando script de análise NLP...") # isso aqui é so p ver se vai carregar msm

# função para análise linguística com spaCy
def analisar_texto(texto):
    doc = nlp(str(texto))
    lemas = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    substantivos = [token.text for token in doc if token.pos_ == "NOUN"]
    verbos = [token.text for token in doc if token.pos_ == "VERB"]
    entidades = [f"{ent.text} ({ent.label_})" for ent in doc.ents]
    return pd.Series({
        "Lemas": ", ".join(lemas),
        "Substantivos": ", ".join(substantivos),
        "Verbos": ", ".join(verbos),
        "Entidades": ", ".join(entidades)
    })

for file_path in input_files:
    if not os.path.exists(file_path):
        print(f"Arquivo não encontrado: {file_path}")
        continue

    print(f"\nProcessando arquivo: {file_path}")
    df = pd.read_csv(file_path)

    # Verifica se a coluna 'Descrição' existe
    if "Descrição" not in df.columns:
        for col in df.columns:
            if col.lower() in ["tweets"]:
                df.rename(columns={col: "Descrição"}, inplace=True)
                print(f"Coluna '{col}' renomeada para 'Descrição'.")
                break
        print(f"Coluna 'Descrição' não encontrada em {file_path}.")
        continue

    # Filtrar com regex
    df_filtrado = df[df["Descrição"].astype(str).str.contains(regex_filtro, flags=re.IGNORECASE, regex=True)]

    if df_filtrado.empty:
        print(f"Nenhuma linha correspondente ao filtro em {file_path}.")
        continue

    # Aplicar análise NLP
    resultado = df_filtrado["Descrição"].apply(analisar_texto)
    df_final = pd.concat([df_filtrado["Descrição"], resultado], axis=1)

    # Criar nome do arquivo de saída
    nome_saida = os.path.splitext(os.path.basename(file_path))[0]  # ex: 'noticias_bets'
    output_path = os.path.join(output_folder, f"analise_{nome_saida}.csv")

    # Salvar resultado
    df_final.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Análise salva com sucesso em: {output_path}")
