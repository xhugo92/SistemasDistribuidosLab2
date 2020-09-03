def interface():
    while True:
        print("Digite o nome do arquivo")
        print("Digite 1 pra sair")
        nome=input()
        if(nome=="1"):
            break
        else:
            print(processo(nome))


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


interface()
