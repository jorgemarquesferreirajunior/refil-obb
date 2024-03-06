import os
import shutil
from zipfile import ZipFile


class UtilitariosArquivo:
    @staticmethod
    def criar_pasta(nome, caminho, verbose=False):
        pasta = os.path.join(caminho, nome)
        if not os.path.exists(pasta):
            os.makedirs(pasta)
        else:
            if verbose:
                print(f"A pasta {nome} já existe.")
        return pasta

    @staticmethod
    def deletar_pasta(caminho_pasta):
        try:
            shutil.rmtree(caminho_pasta)
        except Exception as e:
            print(f"Erro ao excluir a pasta {caminho_pasta}: {e}")

    @staticmethod
    def descompactar_arquivo(arquivo_zip, destino, verbose=False):
        if os.path.exists(os.path.join(destino, "datasets")) and verbose:
            print(f"A pasta já existe neste destino: {os.path.join(destino, 'datasets')}")
        else:
            try:
                with ZipFile(arquivo_zip, "r") as arquivo_zipado:
                    arquivo_zipado.extractall(destino)
                if verbose:
                    print(f"A pasta {arquivo_zip} foi descompactada com sucesso para {destino}.")
            except Exception as e:
                print(f"Erro ao extrair {arquivo_zip}: {e}")
        return os.path.join(destino, "datasets")

    @staticmethod
    def compactar_pasta(origem, destino, nome_arquivo):
        try:
            destino_zip = os.path.join(destino, nome_arquivo + ".zip")
            print(f"A pasta {origem} foi compactada com sucesso para {destino_zip}.")
        except Exception as e:
            print(f"Erro ao compactar {origem}: {e}")

    @staticmethod
    def procurar_pasta(caminho_raiz, pasta_alvo):
        caminhos = []
        for pasta_atual, subpastas, arquivos in os.walk(caminho_raiz):
            if pasta_alvo in subpastas:
                caminhos.append(os.path.join(pasta_atual, pasta_alvo))
        return caminhos if caminhos else None

    @staticmethod
    def procurar_arquivo(caminho_raiz, nome_arquivo, verbose=False):
        for pasta_atual, subpastas, arquivos in os.walk(caminho_raiz):
            if nome_arquivo in arquivos:
                caminho_arquivo = os.path.join(pasta_atual, nome_arquivo)
                if verbose:
                    print(f"O arquivo {nome_arquivo} foi encontrado em: {caminho_arquivo}")
                return caminho_arquivo

        print(f"O arquivo {nome_arquivo} não foi encontrado em {caminho_raiz} ou suas subpastas.")
        return None

    @staticmethod
    def esvaziar_pasta(caminho_pasta):
        dados = os.listdir(caminho_pasta)
        if len(dados) > 0:
            print(f"Encontrados {len(dados)} itens.")
            for item in dados:
                caminho_item = os.path.join(caminho_pasta, item)
                if os.path.isfile(caminho_item):
                    os.remove(caminho_item)
            print("Pasta esvaziada com sucesso!")
        else:
            print("A pasta está vazia!")
            
    @staticmethod
    def listar_imagens_pasta(caminho_pasta):
        return [os.path.join(caminho_pasta, f) for f in os.listdir(caminho_pasta) if f.endswith((".jpg", ".png"))]
    