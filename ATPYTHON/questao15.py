import re
import urllib.request
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

quotes = soup.find_all('div', class_='quote')

# Padrão de limpeza para remover caracteres não alfanuméricos
padrao_limpeza = re.compile(r'[^\w\s]')

# Palavra-chave a ser buscada
palavra_chave = "life"

# Iterar sobre as citações
for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()

    # Limpar o texto da citação
    text_limpo = padrao_limpeza.sub('', text.lower())

    # Verificar se a palavra-chave está na citação
    if palavra_chave in text_limpo:
        print(f"Citação: {text}")
        print(f"Autor: {author}")
        print()  # Linha em branco para melhor legibilidade
