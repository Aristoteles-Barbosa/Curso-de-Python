# Funçaõ perguntar, inserir, pesquisar, excluir e listar

def perguntar():
    resposta = input ("O que deseja realizar? \n" +
                    "<I> - Para inserir um usuario:\n" +
                    "<P> - Para pesquisar um usuário: \n" +
                    "<E> - Para excluir um usuário: \n" +
                    "<L> - Para listar um usuário: \n").upper()
    return resposta 

def inserir (dicionario):
    dicionario [input("Digite o login: ").upper(), 
                input ("Digite a senha: ")] = [input ("Digite o nome:").upper(), 
                                                      input("Digite a útima data de acesso: "), 
                                                      input("Qaul a útima estação acessada: ").upper()]

def pesquisar (dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print ("Nome ......... " + lista [0])
        print ("Ultimo acesso: " + lista [1])
        print ("Ultima estação:" + lista [2])

def excluir (dicionario, chave):
    if dicionario.get (chave) != None:
        del dicionario [chave]
        print ("Objeto eliminado")

def listar (dicionario):
    for chave, valor in dicionario.items():
        print ("Objeto ......")
        print ("Login:", chave)
        print ("Dados:", valor)