import requests as req
from bs4 import BeautifulSoup

url = "https://agenciabrasil.ebc.com.br/busca/site?keys=apostas+manipuladas"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

response = req.get(url)  #print(response) #Testando o responde
if response.status_code == 200:
   soup = BeautifulSoup(response.text, 'html.parser')
#print(soup) #Testando o soup

   artigos = soup.find_all('div', class_="search-results-item")

   for artigo in artigos:
        titulo = artigo.find("h3", class_="search-results-title")
        resumo = artigo.find("div", class_="search-results-summary")
        link= link = titulo.find("a")["href"]

        print("📰 Título:", titulo.get_text(strip=True))
        print("🔗 Link: https://agenciabrasil.ebc.com.br" + link)
        if resumo:
            print("📄 Resumo:", resumo.get_text(strip=True))
        print("-" * 60)
    
else: 
    print("Erro ao acessar a Agência Brasil:", response.status_code)

    