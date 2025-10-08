import pandas as pd
from sqlalchemy import create_engine
import logging

logger = logging.getLogger(__name__)

def salvar_df_sqlite(df, caminho_db, nome_tabela):
    if df is None or df.empty:
        logger.warning(f"Tentativa de salvar DataFrame vazio na tabela {nome_tabela}")
        return
    try:
        engine = create_engine(f'sqlite:///{caminho_db}')
        df.to_sql(nome_tabela, engine, if_exists='replace', index=False)
        logger.info(f"Dados salvos na tabela {nome_tabela}")
    except Exception as e:
        logger.error(f"Erro ao salvar dados na tabela {nome_tabela}: {e}", exc_info=True)

def ler_df_sqlite(caminho_db, nome_tabela):
    try:
        engine = create_engine(f'sqlite:///{caminho_db}')
        df = pd.read_sql_table(nome_tabela, engine)
        logger.info(f"Dados carregados da tabela {nome_tabela}")
        return df
    except Exception as e:
        logger.error(f"Erro ao carregar dados da tabela {nome_tabela}: {e}", exc_info=True)
        return None
