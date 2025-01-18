import pandas as pd
from dotenv import load_dotenv
import os
import pathlib
import logging
import sqlalchemy

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)),'db_secrets.env'))

nome_do_banco = os.environ.get('POSTGRES_DB')
usuario = os.environ.get('POSTGRES_USER')
senha = os.environ.get('POSTGRES_PASSWORD')
host = os.environ.get('HOST')
ENGINE = sqlalchemy.create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}/{nome_do_banco}")

##### Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
    filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'etl.log'),
    filemode='a'
)

def executar_migrations_no_banco_de_dados(sql:str):
    """
    Função responsável por executar comandos SQL no banco.
    """
    try:
        conn = ENGINE.raw_connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        logging.info(f"Executou SQL: {sql}")
    except Exception as e:
        conn.rollback()
        logging.error(f"Erro ao executar SQL: {e}")
    finally:
        cur.close()
        conn.close()

def ler_e_escrever_no_banco_de_dados(caminho_do_arquivo: str, nome_do_schema: str, if_exists: str = "replace"):
    """
    """
    try:
        leitores = {
            "csv": lambda arquivo: pd.read_csv(arquivo, sep=';'),
            "xlsx": pd.read_excel,
            "xls": pd.read_excel,
            "parquet": pd.read_parquet
        }

        extensao = caminho_do_arquivo.split(".")[-1]
        if extensao in leitores:
            base = leitores[extensao](caminho_do_arquivo)
        else:
            logging.error(f"Formato de arquivo '{extensao}' não suportado.")
            return


        ##### CRIANDO SCHEMA CASO ELE NÃO EXISTA AINDA:
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'sql', 'migrations', 'create_schema.sql'), 'r') as arquivo:
            sql = arquivo.read().format(schema=nome_do_schema)
        executar_migrations_no_banco_de_dados(sql)

        if if_exists == "append":
            logging.info("MÉTODO DE ESCRITA É APPEND.")
            executar_migrations_no_banco_de_dados(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                                                    'assets', 
                                                                    'sql', 
                                                                    'migrations', 
                                                                    'delete.sql'), 'r').read().format(schema=nome_do_schema, 
                                                                                                      tabela=os.path.splitext(os.path.basename(caminho_do_arquivo))[0])
                                                                                                        )

        base.to_sql(
            schema=nome_do_schema,
            name=os.path.splitext(os.path.basename(caminho_do_arquivo))[0],
            con=ENGINE,
            index=False,
            if_exists=if_exists
        )
        del base
        logging.info("Processo concluído com sucesso.")
    except Exception as e:
        logging.error(f"Erro: {e}")