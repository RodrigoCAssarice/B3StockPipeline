import os
import logging
from config import configurar_logger
from download import baixar_cotahist
from extract import ler_cotahist
from validate import validar_dados
from transform import filtrar_petr4, calcular_media_mensal
from db import salvar_df_sqlite
import matplotlib.pyplot as plt
import pandas as pd

def plotar_variacao_percentual(df_media):
    try:
        plt.figure(figsize=(12,6))
        plt.plot(df_media['Mes'], df_media['VariacaoPercentual'], marker='o')
        plt.title('Variação Percentual Mensal do Preço Médio Fechamento PETR4')
        plt.xlabel('Mês')
        plt.ylabel('Variação Percentual (%)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        logging.getLogger(__name__).error("Erro ao gerar gráfico", exc_info=True)

def main():
    configurar_logger()
    logger = logging.getLogger(__name__)

    diretorio_download = "./downloads"
    banco_sqlite = "dados_petr4.db"
    anos = [2023, 2024]

    logger.info("Início do processo")

    baixar_cotahist(diretorio_download, anos)

    dfs = []
    for ano in anos:
        caminho_zip = os.path.join(diretorio_download, f"COTAHIST_A{ano}.ZIP")
        df = ler_cotahist(caminho_zip)
        if validar_dados(df):
            dfs.append(df)
        else:
            logger.warning(f"Arquivo do ano {ano} ignorado por falha na validação")

    if not dfs:
        logger.error("Nenhum dado válido para processamento. Abortando.")
        return

    df_total = pd.concat(dfs, ignore_index=True)
    salvar_df_sqlite(df_total, banco_sqlite, "cotahist_bruto")

    df_petr4 = filtrar_petr4(df_total)
    salvar_df_sqlite(df_petr4, banco_sqlite, "cotahist_petr4")

    df_media = calcular_media_mensal(df_petr4)
    if df_media is not None:
        salvar_df_sqlite(df_media, banco_sqlite, "media_mensal_petr4")
        plotar_variacao_percentual(df_media)
    else:
        logger.error("Falha ao calcular médias mensais")

    logger.info("Processo finalizado")

if __name__ == "__main__":
    main()
