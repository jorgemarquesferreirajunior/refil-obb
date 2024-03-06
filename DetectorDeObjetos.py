import cv2
from ultralytics import YOLO
import numpy as np
import math
from CompiladorImagem import *
from UtilitariosArquivo import *
import os


class DetectorObjetos:
    def __init__(self, caminho_modelo):
        self.modelo_yolo = YOLO(caminho_modelo)

    def prever(self, caminho_imagem, limiar_acuracia=0.82):
        imagem = cv2.imread(caminho_imagem)
        resultados_obb = self._resultado_previsao(imagem)
        confiancas, coordenadas = self._obter_dados_objeto(resultados_obb, limiar_acuracia)
        centros = self._calcular_centros(coordenadas)
        coords_ab = self._inverter_eixo_y(coordenadas, imagem.shape[0])
        inclinacoes = self._calcular_inclinacoes(coords_ab)
        
        print(f"Resultados salvis no caminho {pasta_resultados}")
        return confiancas, coordenadas, centros, coords_ab, inclinacoes

    def prever_lista(self, lista_imagens, detector, pasta_resultados, limiar_acuracia=0.85, limpar_pasta_resultados=False):
        if limpar_pasta_resultados:
            UtilitariosArquivo.esvaziar_pasta(pasta_resultados)
            
        confiancas = []
        coordenadas = []
        centros = []
        coords_ab = []
        inclinacoes = []
        
        for img in lista_imagens:
            confianca, coordenada, centro, coord_ab, inclinacao = detector.prever(img, limiar_acuracia=limiar_acuracia)
            confiancas.append(confianca)
            coordenadas.append(coordenada)
            centros.append(centro)
            coords_ab.append(coord_ab)
            inclinacoes.append(inclinacao)
            
            caminho_imagem_resultado = os.path.join(pasta_resultados, f"imagem_compilada_{len(os.listdir(pasta_resultados)) + 1}.jpg")
            CompiladorImagem.gerar_imagem_resultado(cv2.imread(img), centro, coordenada, inclinacao, caminho_imagem_resultado)
        print(f"Resultados salvis no caminho {pasta_resultados}")
        return confiancas, coordenadas, centros, coords_ab, inclinacoes
    
    def _resultado_previsao(self, imagem, ):
        return self.modelo_yolo.predict(source=imagem, save=False)[0].obb

    def _obter_dados_objeto(self, predicao, acuracia):
        confiancas_obb, coords_obb = predicao.conf, predicao.xyxyxyxy

        confiancas_np = self._tensor_para_array(confiancas_obb)
        coords_np = self._tensor_para_array(coords_obb)

        confiancas_float = self._converter_confiancas(confiancas_np)
        coords_int = self._converter_coordenadas(coords_np)

        confiancas_filtradas = []
        coords_filtradas = []

        for indice, valor in enumerate(confiancas_float):
            if valor >= acuracia:
                confiancas_filtradas.append(valor)
                coords_filtradas.append(coords_int[indice])

        return confiancas_filtradas, coords_filtradas

    def _tensor_para_array(self, tensor):
        if isinstance(tensor, np.ndarray):
            return tensor
        elif hasattr(tensor, "numpy"):
            if "cuda" in str(tensor.device):
                tensor = tensor.cpu()
            return tensor.numpy()
        else:
            raise ValueError("Formato de tensor não reconhecido.")

    def _converter_coordenadas(self, lst):
        nova_lista = []
        for id_sub, sublist in enumerate(lst):
            sublist_int = []
            for id_subsub, subsublist in enumerate(sublist):
                subsublist_int = [int(valor) for valor in subsublist]
                sublist_int.append(subsublist_int)
            nova_lista.append(sublist_int)
        return nova_lista

    def _converter_confiancas(self, lst):
        return [round(float(valor), 2) for valor in lst]

    def _calcular_centros(self, coordenadas_int):
        centros = [self._calcular_ponto_medio(sublista[0], sublista[2]) for sublista in coordenadas_int]
        return centros

    def _inverter_eixo_y(self, coordenadas_int, altura_imagem):
        coordenadas = []
        for sublista in coordenadas_int:
            ponto_a = [sublista[0][0], altura_imagem - sublista[0][1]]
            ponto_b = [sublista[3][0], altura_imagem - sublista[3][1]]
            pontos = [ponto_a, ponto_b]
            coordenadas.append(pontos)
        return coordenadas

    def _calcular_inclinacoes(self, coords_ab):
        inclinacoes = [round(self._calcular_angulo(ponto_a, ponto_b), 2) for ponto_a, ponto_b in coords_ab]
        return inclinacoes

    def _calcular_ponto_medio(self, A, B):
        x1, y1 = A
        x2, y2 = B
        return ((x1 + x2) // 2, (y1 + y2) // 2)

    def _calcular_angulo(self, ponto_a, ponto_b):
        ax, ay = ponto_a
        bx, by = ponto_b

        if ay == by:
            return 0
        elif ax == bx:
            return 90
        elif ax < bx:
            delta_x = bx - ax
            if ay < by:
                delta_y = by - ay
                return round(math.degrees(math.atan2(delta_y, delta_x)), 2)
            else:
                delta_y = ay - by
                return 180 - round(math.degrees(math.atan2(delta_y, delta_x)), 2)
        elif ax > bx:
            delta_x = ax - bx
            if ay > by:
                delta_y = ay - by
                return round(math.degrees(math.atan2(delta_y, delta_x)), 2)
            else:
                delta_y = by - ay
                return 180 - round(math.degrees(math.atan2(delta_y, delta_x)), 2)
    
    def gerar_msg(confiancas, centros, inclinacoes):
        mensagem = ''
        for i, (confianca, inclinacao, centro) in enumerate(zip(confiancas, inclinacoes, centros)):
            mensagem += f"deteccao: {i+1} - confianca:{confianca * 100}%\n" + f"centro: {centro}\n" + f"inclinacao: {inclinacao}\n\n"
        return mensagem
