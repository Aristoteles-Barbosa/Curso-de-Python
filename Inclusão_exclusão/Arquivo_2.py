# Funçaõ perguntar, inserir, pesquisar, excluir e listar
def perguntar():
    resposta = input ("O que deseja realizar? \n" +
                    "<I> - Para inserir um usuario\n" +
                    "<P> - Para pesquisar um usuário \n" +
                    "<E> - Para excluir um usuário \n" +
                    "<L> - Para listar um usuário").upper()
    return resposta 