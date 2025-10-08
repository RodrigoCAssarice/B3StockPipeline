import zipfile
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def ler_cotahist(zip_path):
    try:
        with zipfile.ZipFile(zip_path) as z:
            nome_arquivo = [f for f in z.namelist() if f.upper().startswith('COTAHIST') and f.upper().endswith('.TXT')][0]

            widths = [
                2, 8, 6, 12, 3, 12, 2,
                3, 6, 13, 13, 13, 13,
                13, 13, 13, 13, 5, 13, 13
            ]
            df = pd.read_fwf(z.open(nome_arquivo), widths=widths, header=None, encoding='latin1')
            df.columns = [
                "TIPREG", "DATA", "CODBDI", "CODNEG", "TPMERC", "NOMRES", "ESPECI",
                "PRAZOT", "MODREF", "PREABE", "PREMAX", "PREMIN", "PREMED",
                "PREULT", "PREOFC", "PREOFV", "TOTNEG", "QUATOT", "VOLTOT", "PREEX"
            ]
            logger.info(f"Lido arquivo {nome_arquivo} com {len(df)} linhas")
            return df
    except Exception as e:
        logger.error(f"Erro ao ler {zip_path}: {e}", exc_info=True)
        return None
