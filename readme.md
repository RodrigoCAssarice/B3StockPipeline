# Este projeto foi meu primeiro experimento em pipelines de dados. A partir dele, surgiu a ideia de evoluir para o projeto Steam Pipeline, onde estou buscando aplicar arquitetura Bronze/Silver/Gold e práticas modernas de engenharia de dados. Mais alinhadas com o mercado atual.


🚧 WORK IN PROGRESS 🚧

⚠️ **This project is currently under development. Features may be incomplete or subject to change. Contributions and feedback are welcome!**

---

## 📊 Project Overview

This project is a modular scraper designed to automatically download, extract, validate, and transform historical stock data for PETR4 from B3 (Brazilian stock exchange). The goal is to automate the full data pipeline:

- ⬇️ Automatically download .ZIP files with B3 data using Selenium.
- 📥 Extract and load data into pandas DataFrames.
- ✔️ Validate data integrity and quality.
- 📈 Calculate monthly averages and percentage variations of PETR4 closing prices.
- 💾 Save raw and processed data in SQLite database using SQLAlchemy.
- 📊 Generate plots of monthly percentage variations.

---

## 🗂 Project Structure

| File         | Description                                          |
|--------------|------------------------------------------------------|
| `main.py`    | Orchestrates the entire scraping workflow.           |
| `download.py`| Handles downloading files via Selenium.              |
| `extract.py` | Extracts and loads data from ZIP files to DataFrames.|
| `validate.py`| Validates data quality and integrity.                 |
| `transform.py`| Calculates monthly averages and percentage variations.|
| `db.py`      | Functions to save and load data in SQLite via SQLAlchemy.|
| `config.py`  | General settings and logging configuration.           |

---

## ⚙️ Requirements

- Python 3.7+
- Selenium
- pandas
- SQLAlchemy
- matplotlib
- Chrome WebDriver or equivalent

---

## 🚀 How to Use

1. Install the required packages:

   pip install selenium pandas sqlalchemy matplotlib

Download the ChromeDriver compatible with your Chrome browser version and add it to your system PATH.

Run the main script:

python main.py
📞 Contact

Rodrigo Assarice

Email: rodrigo.assarice@hotmail.com



## Portuguese version

📊 Rastreador de Dados - Preços Históricos 
🇧🇷 Versão em Português
Este projeto é um scraper modular desenvolvido para baixar, extrair, validar e transformar dados históricos da ação PETR4 da B3 (Bolsa de Valores do Brasil). O objetivo é automatizar o fluxo completo:

⬇️ Baixar automaticamente os arquivos .ZIP com os dados da B3 usando Selenium.

📥 Extrair e importar os dados para DataFrames pandas.

✔️ Validar a integridade e qualidade dos dados.

📈 Calcular médias mensais e variações percentuais dos preços de fechamento da ação PETR4.

💾 Salvar os dados brutos e processados em banco SQLite usando SQLAlchemy.

📊 Gerar gráficos das variações percentuais mensais.

🗂 Estrutura do projeto
Arquivo	Descrição
main.py	Orquestra todo o fluxo do scraper.
download.py	Responsável por baixar os arquivos usando Selenium.
extract.py	Extrai e importa os dados do arquivo ZIP para DataFrame.
validate.py	Valida a qualidade e integridade dos dados.
transform.py	Calcula médias mensais e variações percentuais.
db.py	Funções para salvar e ler dados em banco SQLite com SQLAlchemy.
config.py	Configurações gerais e logging.

⚙️ Requisitos
Python 3.7+

Selenium

pandas

SQLAlchemy

matplotlib

WebDriver Chrome ou equivalente

🚀 Como usar
Configure o ambiente instalando os pacotes necessários:

bash
Copiar código
pip install selenium pandas sqlalchemy matplotlib
Baixe o driver do Chrome (ChromeDriver) compatível com sua versão do navegador e coloque no PATH do sistema.

Execute o script principal:


python main.py
Os dados serão baixados, processados e armazenados no banco dados_petr4.db. O gráfico das variações mensais será exibido ao final.

---

