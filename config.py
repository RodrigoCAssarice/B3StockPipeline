import logging

def configurar_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("scraper.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
