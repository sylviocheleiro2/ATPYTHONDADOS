from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar opções do webdriver para o modo headless
options = Options()
options.add_argument('--headless')  # Modo headless
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--incognito')  # Modo anônimo

# Iniciar o ChromeDriver
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

# URL da página de avaliações do livro
url = 'https://www.amazon.com.br/Web-Scraping-Python-Ryan-Mitchell/product-reviews/1491985577/ref=cm_cr_unknown?ie=UTF8&reviewerType=all_reviews&pageNumber=1&filterByStar=five_star'

# Abrir a URL
driver.get(url)

try:
    # Aguardar até que o elemento esteja presente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//span[@class="a-list-item"]/a[@class="a-link-normal"]'))
    )

    # Encontrar o título do livro usando o novo XPath
    book_title_element = driver.find_element(
        By.XPATH, '//span[@class="a-list-item"]/a[@class="a-link-normal"]')

    # Extrair e imprimir o texto
    book_title = book_title_element.text.strip()
    print(f"Nome do Livro: {book_title}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fechar o navegador
    driver.quit()
