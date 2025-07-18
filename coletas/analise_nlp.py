import pandas as pd
import spacy
import os

# modelo de português do spaCy
nlp = spacy.load("pt_core_news_sm")

# caminhos de entrada e saída
input_path = "noticias_bets.csv"
output_path = os.path.join("resultados", "analise_nlp.csv")

# carregar os dados
df = pd.read_csv(input_path)

print("Iniciando script de análise NLP...") # isso aqui é so p ver se vai carregar msm

if not os.path.exists(input_path):
    print(f"Arquivo não encontrado em: {input_path}")
    exit()
else:
    print(f"Arquivo encontrado: {input_path}")

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

# aplicar a análise na coluna de descrição
resultado = df["Descrição"].apply(analisar_texto)

# concatenar resultados com texto original
df_final = pd.concat([df["Descrição"], resultado], axis=1)

# salvar arquivo final
os.makedirs("resultados", exist_ok=True)
df_final.to_csv(output_path, index=False, encoding="utf-8")

print(f"Análise linguística salva com sucesso em: {output_path}")
