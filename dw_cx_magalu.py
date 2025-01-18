import logging
import os
from datetime import datetime
from utils.ambiente_virtual import AmbienteVirtual
from utils.inicializador import instalar_dependencias, iniciar_docker
from utils.extract import extrair_dados_do_big_query
from utils.load import ler_e_escrever_no_banco_de_dados, executar_migrations_no_banco_de_dados

MES_ATUAL = datetime.now().strftime("%Y_%m")
CAMINHO_DE_CONSULTAS_SQL_PARA_EXTRAIR = os.path.join(os.path.dirname(__file__), 'assets', 'sql', 'extract')
CAMINHO_DE_DADOS_RAW = os.path.join(os.path.dirname(__file__), 'assets', 'data', 'raw', MES_ATUAL)
CAMINHO_DE_CONSULTAS_SQL_PARA_MODELAGEM_TREATED = os.path.join(os.path.dirname(__file__), 'assets', 'sql', 'transform')

def main() -> None:
    """
    Função responsável pela execução completa do código através do ambiente virtual.

    Essa função tem o objetivo de: Cria, ativar e desativar o ambiente virtual.
    """
    
    iniciar_docker()
    logging.info('LOG - INICIANDO ETL ...')

    ##### CHAMANDO FUNÇÃO DE EXTRAÇÃO 
    for arquivo in os.listdir(CAMINHO_DE_CONSULTAS_SQL_PARA_EXTRAIR):
        extrair_dados_do_big_query(
        caminho_da_consulta_sql=os.path.join(CAMINHO_DE_CONSULTAS_SQL_PARA_EXTRAIR, arquivo),
        projeto_do_big_query='projeto_do_bigquery')

    ##### CHAMANDO FUNÇÃO DE CARGA NO BANCO PARA CAMADA RAW
    for arquivo in os.listdir(CAMINHO_DE_DADOS_RAW):
        ler_e_escrever_no_banco_de_dados(
            caminho_do_arquivo=os.path.join(CAMINHO_DE_DADOS_RAW, arquivo),
            nome_do_schema='dw_cx_magalu_raw',
            if_exists='replace'
        )                
    #### CHAMANDO FUNÇÃO DE TRANFORMAÇÃO OU MODELAGEM DE DADOS 
    for arquivo in os.listdir(CAMINHO_DE_CONSULTAS_SQL_PARA_MODELAGEM_TREATED):
        executar_migrations_no_banco_de_dados(
            sql=open(os.path.join(CAMINHO_DE_CONSULTAS_SQL_PARA_MODELAGEM_TREATED, arquivo)).read()
        )


if __name__ == "__main__":
    main()
