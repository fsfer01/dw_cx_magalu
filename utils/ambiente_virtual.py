import os
import sys
import subprocess
import platform
from pathlib import Path

class AmbienteVirtual:
    def __init__(self, nome_venv="venv"):
        self.nome_venv = nome_venv
        self.caminho_ambiente = Path(__file__).resolve().parent.parent / nome_venv
        self.pip_venv = None

    def criar(self):
        """
        Função responsável pela criação do ambiente virtual.
        """
        try:
            if not self.verificar_existencia():
                subprocess.run([sys.executable, "-m", "venv", str(self.caminho_ambiente)])
                print(f"Ambiente virtual '{self.nome_venv}' criado com sucesso!")
            else:
                print(f"Ambiente virtual '{self.nome_venv}' já existe!")
        except Exception as e:
            print(f"Erro ao criar ambiente virtual: {e}")

    def ativar(self):
        """
        Função responsável pela ativação do ambiente virtual.
        """
        try:
            if self.verificar_existencia():
                if platform.system().lower() == "windows":
                    ativador = f'"{self.caminho_ambiente}/Scripts/activate"'
                    subprocess.run(ativador, shell=True)
                    self.pip_venv = str(self.caminho_ambiente / "Scripts" / "pip.exe")
                else:
                    ativador = f'source "{self.caminho_ambiente}/bin/activate"'
                    subprocess.run(["bash", "-c", ativador])
                    self.pip_venv = str(self.caminho_ambiente / "bin" / "pip")
                print(f"Ambiente virtual '{self.nome_venv}' ativado com sucesso!")
            else:
                print(f"Ambiente virtual '{self.nome_venv}' não encontrado!")
        except Exception as e:
            print(f"Erro ao ativar ambiente virtual: {e}")

    def desativar(self):
        """
        Função responsável pela desativação do ambiente virtual.
        """
        try:
            if platform.system().lower() == "windows":
                desativador = f'"{self.caminho_ambiente}/Scripts/deactivate.bat"'
            else:
                desativador = "deactivate"
            subprocess.run(desativador, shell=True)
            print(f"Ambiente virtual '{self.nome_venv}' desativado com sucesso!")
        except Exception as e:
            print(f"Erro ao desativar ambiente virtual: {e}")

    def verificar_existencia(self):
        """
        Função responsável pela verificação da existência do ambiente virtual.
        """
        return self.caminho_ambiente.exists()

    def executar_codigo(self, codigo):
        """
        Função responsável pela execução do código no ambiente virtual.
        """
        python_venv = f"{self.caminho_ambiente}/bin/python"
        self.ativar()
        exec(codigo)

    def executar_arquivo(self, arquivo):
        """Executa arquivo no ambiente virtual."""
        python_venv = f"{self.caminho_ambiente}/bin/python"
        self.ativar()
        subprocess.run([python_venv, arquivo])

    def executar_funcao(self, funcao):
        """Executa função no ambiente virtual."""
        self.ativar()
        funcao()