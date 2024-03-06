from UtilitariosArquivo import UtilitariosArquivo as UA

imagens = UA.listar_imagens_pasta("C:\\Users\\engen\\Documents\\GitHub\\Scope\\YOLO\\refil-poo\\datasets\\test\\images")

print('\n')
for img in imagens:
    print(img)
print('\n')