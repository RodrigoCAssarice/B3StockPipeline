import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

logger = logging.getLogger(__name__)

def baixar_cotahist(diretorio_download, anos):
    logger.info("Iniciando download dos arquivos COTAHIST")
    options = Options()
    options.add_argument("--headless")
    prefs = {"download.default_directory": os.path.abspath(diretorio_download)}
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(options=options)
    try:
        if not os.path.exists(diretorio_download):
            os.makedirs(diretorio_download)
            logger.info(f"Diretório criado: {diretorio_download}")
        
        for ano in anos:
            url = f"https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A{ano}.ZIP"
            logger.info(f"Baixando arquivo: {url}")
            driver.get(url)
            time.sleep(8)  # Ajuste o tempo conforme a velocidade da sua conexão
        logger.info("Download finalizado.")
    except Exception as e:
        logger.error("Erro ao baixar arquivos", exc_info=True)
    finally:
        driver.quit()
