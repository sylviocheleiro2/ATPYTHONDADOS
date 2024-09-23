import requests
from bs4 import BeautifulSoup
import re

# URL da página que contém a tabela
url = 'https://www.gutenberg.org/browse/scores/top'

# Fazer a requisição para obter o conteúdo da página
response = requests.get(url)
response.raise_for_status()  # Levanta um erro se a requisição falhar

# Parsear o conteúdo da página com BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Estrutura para armazenar os dados extraídos
downloads_data = {}

# Encontrar todos os links com downloads
for link in soup.find_all('a', href=re.compile(r'/ebooks/\d+')):
    text = link.text.strip()
    # Usar regex para capturar a quantidade de downloads
    match = re.search(r'\((\d+)\)', text)
    if match:
        downloads = int(match.group(1))  # Captura a quantidade
        title = text.split(' (')[0]  # Pega o título do livro
        downloads_data[title] = downloads  # Armazena no dicionário

# Ordenar por downloads e limitar aos 100 primeiros
sorted_downloads = sorted(downloads_data.items())

# Imprimir os dados no formato desejado
for title, downloads in sorted_downloads:
    print(f"{title} - Downloads {downloads}")
    print(f"Link: https://www.gutenberg.org/ebooks/{downloads}")
