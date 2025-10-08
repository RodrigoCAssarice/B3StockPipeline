# logger_config.py
import logging

def configurar_logger(nome_arquivo="scraper.log"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(nome_arquivo, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger()
    return logger
