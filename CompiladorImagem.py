import cv2
from ProcessadorDeImagem import *

class CompiladorImagem:
    @staticmethod
    def gerar_imagem_resultado(imagem, centros, coordenadas, inclinacoes, resultado="resultado.jpg"):
        ProcessadorImagem.enumerar_centros(imagem, centros)
        ProcessadorImagem.marcar_caixas(imagem, coordenadas)
        ProcessadorImagem.listar_inclinacoes(imagem, inclinacoes)
        cv2.imwrite(resultado, imagem)
