import pandas as pd
import logging

def filtrar_petr4(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra registros da ação PETR4. Sanitiza a coluna CODNEG antes.
    """
    if df.empty:
        logging.warning("DataFrame de entrada está vazio.")
        return pd.DataFrame()

    # Sanitize: remove espaços, letras minúsculas, valores nulos etc.
    df["CODNEG"] = df["CODNEG"].astype(str).str.strip().str.upper()

    df_petr4 = df[(df["CODNEG"] == "PETR4") & (df["TIPREG"] == "01")]

    logging.info(f"Registros PETR4 filtrados: {len(df_petr4)}")
    return df_petr4


def calcular_media_mensal(df_petr4: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a média mensal do preço de fechamento da PETR4.
    """
    if df_petr4.empty:
        logging.warning("DataFrame PETR4 está vazio. Pulando cálculo de média.")
        return pd.DataFrame()

    # Garantir tipo datetime
    df_petr4["DATA"] = pd.to_datetime(df_petr4["DATA"], format="%Y%m%d")

    # Converter valores de centavos para reais
    df_petr4["PREULT"] = df_petr4["PREULT"].astype(float) / 100

    # Agrupar por mês e calcular média
    media_mensal = (
        df_petr4
        .set_index("DATA")
        .resample("M")["PREULT"]
        .mean()
        .reset_index()
        .rename(columns={"DATA": "Mes", "PREULT": "PrecoMedioFechamento"})
    )

    logging.info("Cálculo de médias mensais concluído")
    return media_mensal


def calcular_variacao_percentual(media_mensal: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a variação percentual mês a mês da média de fechamento.
    """
    if media_mensal.empty:
        logging.warning("DataFrame de médias mensais está vazio. Sem variação calculada.")
        return pd.DataFrame()

    media_mensal["VariacaoPercentual"] = media_mensal["PrecoMedioFechamento"].pct_change() * 100
    media_mensal["VariacaoPercentual"] = media_mensal["VariacaoPercentual"].round(2)

    return media_mensal
