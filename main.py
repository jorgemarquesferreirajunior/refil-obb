from CapturaCamera import *
from ClienteTCP import *
from CompiladorImagem import *
from DetectorDeObjetos import *
from UtilitariosArquivo import *

PASTA_HOME = os.getcwd()
CAMINHO_CONJUNTO_DADOS = UtilitariosArquivo.descompactar_arquivo(os.path.join(PASTA_HOME, "imagens.zip"), PASTA_HOME)

caminho_modelo = UtilitariosArquivo.procurar_arquivo(CAMINHO_CONJUNTO_DADOS, 'best.pt')
caminho_resultados = UtilitariosArquivo.criar_pasta('resultados', PASTA_HOME)
detector_objetos = DetectorObjetos(caminho_modelo)

#----------------------------------------------------------------------------------------------------------------------------------------
# prever um pacote de imagens de uma base de dados
IMAGENS_TESTE = UtilitariosArquivo.listar_imagens_pasta(os.path.join(CAMINHO_CONJUNTO_DADOS, 'test', 'images'))
lista_confiancas, lista_coordenadas, lista_centros, lista_coords_ab, lista_inclinacoes = detector_objetos.prever_lista(IMAGENS_TESTE, detector_objetos, caminho_resultados, limiar_acuracia=0.81, limpar_pasta_resultados=True)
#----------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------
#  prever uma imagem de uma captura
# ip_camera = "http://192.168.0.103:8080/video"
# caminho_capturas = UtilitariosArquivo.criar_pasta("capturas", PASTA_HOME)
# imagem = CapturaCamera.tirar_foto(ip_camera, caminho_capturas)
# confiancas, coordenadas, centros, coords_ab, inclinacoes = detector_objetos.prever(imagem)
# caminho_imagem_resultado = os.path.join(caminho_resultados, f"imagem_compilada_{len(os.listdir(caminho_resultados)) + 1}.jpg")
# CompiladorImagem.gerar_imagem_resultado(cv2.imread(imagem), centros, coordenadas, inclinacoes, caminho_imagem_resultado)
#----------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------
#  prever uma imagem de uma base de dados
# imagem = "/home/marks/codes/YOLO/refil-poo/datasets/test/images/37_jpg.rf.a4c23f3c139973b93654f341314c1a44.jpg"
# confiancas, coordenadas, centros, coords_ab, inclinacoes = detector_objetos.prever(imagem, limiar_acuracia=0.81)
# caminho_imagem_resultado = os.path.join(caminho_resultados, f"imagem_compilada_{len(os.listdir(caminho_resultados)) + 1}.jpg")
# CompiladorImagem.gerar_imagem_resultado(cv2.imread(imagem), centros, coordenadas, inclinacoes, caminho_imagem_resultado)

# mensagem = DetectorObjetos.gerar_msg(confiancas, centros, inclinacoes)
# print(mensagem)
#----------------------------------------------------------------------------------------------------------------------------------------

# UtilitariosArquivo.esvaziar_pasta(caminho_resultados)
# UtilitariosArquivo.esvaziar_pasta(caminho_capturas)