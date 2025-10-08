import logging

logger = logging.getLogger(__name__)

def validar_dados(df):
    if df is None:
        logger.warning("DataFrame é None")
        return False
    
    if df.empty:
        logger.warning("DataFrame está vazio")
        return False
    
    colunas_esperadas = [
        "TIPREG", "DATA", "CODBDI", "CODNEG", "TPMERC", "NOMRES", "ESPECI",
        "PRAZOT", "MODREF", "PREABE", "PREMAX", "PREMIN", "PREMED",
        "PREULT", "PREOFC", "PREOFV", "TOTNEG", "QUATOT", "VOLTOT", "PREEX"
    ]

    if not all(col in df.columns for col in colunas_esperadas):
        logger.warning("DataFrame não contém todas as colunas esperadas")
        return False

    logger.info("Validação dos dados OK")
    return True
