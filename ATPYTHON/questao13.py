import requests
from bs4 import BeautifulSoup

# URL da página que contém a tabela
url = 'https://www.gutenberg.org/browse/scores/top'

# Fazer a requisição para obter o conteúdo da página
response = requests.get(url)
response.raise_for_status()  # Levanta um erro se a requisição falhar

# Parsear o conteúdo da página com BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar a tabela de downloads
downloads_table = soup.find('table')  # Encontre a tabela sem depender de tbody

# Verificar se a tabela foi encontrada
if downloads_table is None:
    print("Tabela não encontrada. Verifique a estrutura da página.")
else:
    # Estrutura para armazenar os dados extraídos
    downloads_data = []

    # Iterar sobre as linhas da tabela, ignorando o cabeçalho
    # Ignora a primeira linha (cabeçalho)
    for row in downloads_table.find_all('tr')[1:]:
        columns = row.find_all('td')
        if columns:
            date = row.find('th').text.strip()  # A data está na <th>
            downloads = columns[0].text.strip().replace(
                ',', '')  # Downloads estão na primeira <td>
            downloads_data.append((date, int(downloads)))

    # Imprimir os dados extraídos
    for date, downloads in downloads_data:
        print(f"Data: {date}, Downloads: {downloads}")
