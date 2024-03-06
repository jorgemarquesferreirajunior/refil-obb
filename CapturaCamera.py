import cv2
import os

class CapturaCamera:
    @staticmethod
    def tirar_foto(ip_camera, destino, altura_imagem=640, rotacao=cv2.ROTATE_90_CLOCKWISE):
        captura = cv2.VideoCapture(ip_camera)

        if not captura.isOpened():
            print("Erro ao abrir a câmera.")
            exit()

        while True:
            sucesso, frame = captura.read()

            if not sucesso:
                print("Erro ao ler o frame.")
            else:
                largura, altura = frame.shape[1], frame.shape[0]
                proporcao_tela = largura / altura
                largura_imagem = int(proporcao_tela * altura_imagem)

                frame = cv2.resize(frame, (largura_imagem, altura_imagem))
                frame = cv2.rotate(frame, rotacao)
                frame = frame[:altura_imagem, :altura_imagem]
                item = len(os.listdir(destino)) + 1
                cv2.imwrite(os.path.join(destino, f"foto({str(item)}).jpg"), frame)
                print("Foto salva com sucesso!")
            return os.path.join(destino, f"foto({str(item)}).jpg")
