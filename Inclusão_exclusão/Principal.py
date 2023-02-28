from Principal import*

# Digitar as opções inclusão, pesquisar, eclusão e listar

usuarios = {}
opcao = perguntar ()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    
    if opcao == "I":
        inserir (usuarios)
    
    if opcao == "P":
        pesquisar (usuarios, input ("Qual login deseja pesquisar? "))

    if opcao =="E":
        excluir (usuarios.input("Qual login deseja pesquisar? "))
    
    if opcao == "L":
        listar (usuarios)

    opcao = perguntar ()

# Chamar a função do arquivo 2
