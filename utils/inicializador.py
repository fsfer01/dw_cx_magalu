import subprocess
import os
import sys
import logging
import pathlib

CAMINHO_DOCKER = str(pathlib.Path(__file__).parent.parent / 'docker-compose.yml')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
    filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'etl.log'),
    filemode='a'
)

def instalar_dependencias(pip_venv:str):
    """
    Função responsável por instalar todas as bibliotecas necessárias que estão no requirements no ambiente virtual.
    """
    logging.info(f"INICIANDO PROCESSO DE INSTALAÇÃO DE DEPENDÊNCIAS.")

    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "requirements.txt"), 'r') as f:
        dependencias = [linha.strip() for linha in f.readlines()]
    for dependencia in dependencias:
        logging.info(f"INSTALANDO {dependencia}...")
        try:
            subprocess.check_call([pip_venv, "install", dependencia])
        except subprocess.CalledProcessError as e:
            logging.error(f"ERRO AO INSTALAR {dependencia}: {e}")

def iniciar_docker():
    """
    Função responsável pela inicialização do docker.
    """    
    logging.info(f"INICIANDO DOCKER...")
    if sys.platform == "win32":
        subprocess.run(["docker", "compose", "-f", CAMINHO_DOCKER, "up", "-d"])
    else:
        subprocess.run(["docker", "compose", "-f", CAMINHO_DOCKER, "up", "-d"])        
    logging.info(f"DOCKER INICIADO COM SUCESSO")
