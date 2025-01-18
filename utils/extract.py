import os
import pandas as pd
from datetime import datetime
from pandas.io import gbq
from oauth2client.service_account import ServiceAccountCredentials

MES_ATUAL = datetime.now().strftime("%Y_%m")
CAMINHO = os.path.join(os.path.dirname(os.getcwd()),'dw_cx_magalu','assets','data','raw')

##### CRIA PASTA PARA ARMAZENAR EXTRAÇÕES
os.makedirs(os.path.join(CAMINHO,MES_ATUAL), exist_ok=True)

def extrair_dados_do_big_query(caminho_da_consulta_sql:str,projeto_do_big_query:str):    
    """
    Função responsável por realizar uma consulta no BIGQUERY. O resultado será armazenado em um CSV na pasta assets/data
    """  
    consulta_sql = open(caminho_da_consulta_sql, 'r').read()
    extracao = gbq.read_gbq(consulta_sql, project_id=projeto_do_big_query, dialect='standard')
    extracao.to_csv(os.path.join(CAMINHO, MES_ATUAL, f"{os.path.splitext(os.path.basename(caminho_da_consulta_sql))[0]}.csv"), sep=';', encoding="UTF-8", index=False)