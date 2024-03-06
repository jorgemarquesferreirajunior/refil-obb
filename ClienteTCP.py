from socket import *
from time import sleep

class ClienteTcp:
    def __init__(self, ip_servidor, porta):
        self.ip_servidor = ip_servidor
        self.porta = porta
        self.cliente = socket(AF_INET, SOCK_STREAM)
        self.cliente.connect((ip_servidor, porta))

    def enviar_mensagem(self, mensagem):
        self.cliente.send(mensagem.encode())

class ServidorTcp:
    def __init__(self, ip_servidor, porta):
        self.ip_servidor = ip_servidor
        self.porta = porta
        self.servidor = socket(AF_INET, SOCK_STREAM)
        self.servidor.bind((self.ip_servidor, self.porta))
        self.servidor.listen(1)
        
    def start(self):
        while True:
            conexao, _ = self.servidor.accept()
            msg_anteirior = ''
            while True:
                msg_nova = conexao.recv(1024).decode()
                if msg_nova != msg_anteirior:
                    msg_anteirior = msg_nova
                    print(f"cliente: {msg_nova}")
