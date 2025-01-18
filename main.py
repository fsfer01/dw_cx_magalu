import os
import sys
from utils.ambiente_virtual import AmbienteVirtual
from utils.inicializador import instalar_dependencias

def main():
    """
    Essa função é a função responsável pela execução do projeto. Através dessa função, é feito:
    1-Criação do ambiente virtual.
    2-Ativação do ambiente virtual.
    3-Instalação de dependências no ambiente virtual.
    4-Execução do projeto no ambiente virtual.
    5-Desativação do ambiente virtual.    
    """
    av = AmbienteVirtual()
    av.criar()
    av.ativar()
    instalar_dependencias(av.pip_venv)
    
    ##### CAMINHO DO PYTHON DO AMBIENTE VIRTUAL
    python_venv = os.path.join(av.caminho_ambiente, 'bin', 'python')

    ##### CÓDIGO QUE DEVE SER EXECUTADO NO AMBIENTE VIRTUAL
    dw_cx_magalu_py = os.path.join(os.path.dirname(__file__), 'dw_cx_magalu.py')
    
    try:
        os.system(f'"{python_venv}" "{dw_cx_magalu_py}"')
    except subprocess.SubprocessError as e:
        print(f"Erro: {e}")

    av.desativar()  

if __name__ == "__main__":
    main()