from csv import writer
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_page(url):
    """ Inicializa o WebDriver(Navegador) e acessa a página."""
    print('Iniciou o fetch_page')
    #Configuração das opções do Chrome 
    chrome_options = webdriver.ChromeOptions() #Criação do Objeto de configuração do Chrome no webdriver 
    chrome_options.add_argument('headless') # Roda em modo headless( Não necessário abrir o navegador)
    chrome_options.add_argument("--no-sandbox") # é uma camada de segurança do Chrome que impede que processos maliciosos afetem o sistema.
    
    #Inicialização do WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service, options = chrome_options) # Inicialização do WebDriver com as configurações do navegador

    driver.get(url)
   
    wait = WebDriverWait(driver, 10) # Espera até 10 segundos para que o elemento esteja
    page_source = driver.page_source # Pegar o conteúdo da página
   
    driver.quit()

 
    return page_source