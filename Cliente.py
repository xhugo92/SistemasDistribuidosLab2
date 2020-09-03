import socket

HOST='localhost'
PORTA = 7000
sock= socket.socket()
sock.connect((HOST,PORTA))
while True:
    print("Digite o(s) nome(s) do(s) arquivo(s) separado por espaço")
    print("Digite 1 pra sair")
    entrada = input()
    if(entrada=="1"):
        break
    sock.send(bytes(entrada,'utf-8'))
    mensagens = len(entrada.split(" "))
    aux=0
    while aux<mensagens:
        msg = sock.recv(1024)
        print(str(msg, encoding= 'utf-8'))
        aux+=1

sock.close()
