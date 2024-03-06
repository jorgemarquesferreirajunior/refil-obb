import cv2

class ProcessadorImagem:
    @staticmethod
    def marcar_centros(imagem, centros, raio=5, cor=(0, 0, 255)):
        for centro in centros:
            cv2.circle(imagem, centro, raio, cor, cv2.FILLED)

    @staticmethod
    def enumerar_centros(imagem, centros, cor=(0, 0, 255)):
        for idx, centro in enumerate(centros):
            cv2.putText(imagem, f"{str(idx+1)}", centro, cv2.FONT_HERSHEY_SIMPLEX, 1, cor, 2)

    @staticmethod
    def listar_inclinacoes(imagem, inclinacoes, cor=(0, 0, 255)):
        x_pos = 15
        y_pos = 25

        cor2 = (50, 50, 255)
        cv2.putText(imagem, f"Img | Angulo", (x_pos, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 1, cor, 2)
        y_pos += 35
        for idx, inclinacao in enumerate(inclinacoes):
            cv2.putText(imagem, f"  {str(idx+1)}   {str(inclinacao)}", (x_pos, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 1, cor2, 2)
            y_pos += 30

    @staticmethod
    def marcar_caixas(imagem, coordenadas, cor=(0, 0, 255)):
        for pontos in coordenadas:
            p1, p2, p3, p4 = tuple(pontos[0]), tuple(pontos[1]), tuple(pontos[2]), tuple(pontos[3])
            cv2.line(imagem, p1, p2, cor, 1)
            cv2.line(imagem, p2, p3, cor, 1)
            cv2.line(imagem, p3, p4, cor, 1)
            cv2.line(imagem, p4, p1, cor, 1)

    @staticmethod
    def marcar_inclinacoes(imagem, inclinacoes, centros):
        for idx, inclinacao in enumerate(inclinacoes):
            cv2.putText(imagem, f"{str(inclinacao)}", (centros[idx][0] + 10, centros[idx][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

