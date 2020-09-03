import socket
import json

def processo(nome):
    dic={}
    lista=abrearquivo(nome)
    if(type(lista)==str):
        return lista
    else:
        for x in lista:
            aux=x.split(" ")
            for y in aux:
                y=y.strip('\n')
                if dic.get(y)==None:
                    dic[y]=1
                else:
                    dic[y]=dic[y]+1
        return dic
                

def abrearquivo(nome):
    try:
        arq=open(nome,'r')
        return arq.readlines()
    except:
        return "Erro, arquivo não encontrado"


HOST = ''
PORTA = 7000

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORTA))
sock.listen(1)
nsock, endereco = sock.accept()
while True:
    msg= nsock.recv(1024)
    if not msg:
        break
    msg=str(msg, encoding='utf-8').split(" ")
    retornos=[]
    for x in msg:
        print("Processando "+x)
        retornos.append(processo(x))
    for x in retornos:
        if type(x)==str:
            print("enviando string")
            nsock.send(bytearray(x,'utf-8'))
        if type(x)==dict:
            print("enviando dicionario")
            nsock.send(bytearray(json.dumps(x),'utf-8'))
nsock.close()
sock.close()
