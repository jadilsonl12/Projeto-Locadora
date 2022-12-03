import os

banco_Cadastro = []
galeria_de_filmes = ['O poderoso chefão', 'O rei leão', 'O senhor dos anéis: o retorno do rei', 'À espera de um milagre', 'Vingadores: Ultimato', 'Batman - O cavaleiro das trevas', 'A vida é bela', 'O poderoso chefão 2', 'Vingadores: Guerra infinita', 'Viva -  A vida é uma festa', 'De volta para o futuro']
filmes_lancados_recentemente = ['Sorria', 'Uncharted: Fora do mapa', 'Órfã 2: A origem', 'Jurassic World', 'Top gun: Maverick', 'The Batman', 'Homem Aranha: Sem volta pra casa', 'Thor Amor e Trovão', 'Velozes e Furiosos 9', 'Terrifeir']
filmes_atualmente_reservados = []
minha_lista_de_filmes = []
estoque_de_filmes =  filmes_lancados_recentemente + galeria_de_filmes

def cadastro():

    while True:
        print("# Digite suas informações #")
        print("\n")

        dados = {}
        dados['nome'] = str(input("Digite seu nome: "))
        dados['senha'] = input("Digite uma senha (Obs: contendo apenas números): ")
        dados['email'] = input("Digite seu email: ")
        
        lista = {i['email']: i for i in banco_Cadastro} #verifica repetições por meio das chaves
        while dados['email'] in lista: #caso já esteja em uso, solicita um nome email
            dados['email'] = input("E-mail já está sendo usado, digite outro E-mail: ")

        dados['login'] = input("Digite seu login: ")
        lista = {i['login']: i for i in banco_Cadastro}
        while dados['login'] in lista:
            dados['login'] = input("Login já está sendo usado, digite outro: ")

        banco_Cadastro.append(dados)

        print("Cadastro realizado com sucesso!\n")

        opcao = input("Deseja realizar mais um cadastro? (s/n): ")
        if(opcao == 'n'): 
            inicio()
            break

def login():

    while True:

        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
    
        lista = {i['login']: i for i in banco_Cadastro} #verifica repetições por meio das chaves
        lista1 = {i['senha']: i for i in banco_Cadastro} #verifica repetições por meio das chaves

        if login in lista and senha in lista1:
            print("Login efetuado com sucesso!")
            
            tela_inicio()
            break
        else:
            print("Login ou senha não encontrado!")

            opcao = input("Deseja voltar ao inicio? (s/n)")
            if(opcao == 's'): 
                inicio()
                break
            
def dadosUsuarios():

    while True:
        print("Digite o login que deseja buscar: ")
        lista = {i['login']: i for i in banco_Cadastro}

        pesquisa = input("Login: ")

        if pesquisa in lista:
            print(f"Dados dos usuário [{pesquisa}]: {lista[pesquisa]}")
        else:
            print("Usuário não encontrado!")

        opcao = input("Deseja consultar outro usuário? (s/n)")
        if(opcao == 'n'): 
            inicio()
            break

def mostrarUsuario():

    while True:

        print("# Usuários cadastrados #")

        for i in banco_Cadastro:

            print('Nome:', i['nome'], 'Login: ', i['login'] )
        
        opcao = input("Deseja consultar novamente? (s/n)")
        if(opcao == 'n'): 
            inicio()
            break

def excluir_Usuario():

    while True:
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
    
        for i in range(len(banco_Cadastro)):
            element = banco_Cadastro[i]
            if element["login"] == login and element["senha"] == senha:
                banco_Cadastro.pop(i)
                print("Usuário excluído!")
                break
        else:
            print("Usuário não encontrado!")

        opcao = input("Deseja excluir outro usuário? (s/n)")
        if(opcao == 'n'): 
            inicio()
            break
         
def inicio():

    print("#### LOCADORA DE VÍDEO ####")
    print("\n")
    print("1) Cadastrar-se")
    print("2) Efetuar login")
    print("3) Consultar usuários")
    print("4) Consultar banco de dados")
    print("5) Excluir usuário")
    print("6) Sair\n")

def tela_inicio():

    print("\n")
    print("O que deseja?")

    print("1 - Ver Estoque de filmes")
    print("2 - Ver Filmes lançados recentemente ")
    print("3 - Ver Filmes atualmente reservados")
    print("4 - Alugar filmes ")
    print("5 - Ver total a pagar")
    print("6 - Voltar para tela de início")

    while True:

        opcao2 = int(input("Escolha uma das opções: "))

        if opcao2 > 6 or opcao2 < 0:
            print("Erro, tente novamente")
            tela_inicio()

        if(opcao2 == 1):

            print("\n")
            for i in estoque_de_filmes:
                print(i)
            
        elif(opcao2 == 2):

            print("\n")
            for i in filmes_lancados_recentemente:
                print(i)

        elif(opcao2 == 3):
            for i in minha_lista_de_filmes:
                print(i)

        elif(opcao2 == 4):
            busca = input(print("Qual filme deseja buscar? "))
            filme_encontrado = False

            for i in range(len(estoque_de_filmes)):
                filme = estoque_de_filmes[i]
                if filme == busca:
                    print("Filme encontrado!")
                    filme_encontrado = True
                    opcao3 = input("Deseja alugar? (s/n)")
                    if(opcao3 == 's'):
                        alugar(filme)
                    if(opcao3 == 'n'):
                        tela_inicio()
                    break

            if not filme_encontrado:
                print("Filme não encontrado!")
                tela_inicio()
                break
        elif(opcao2 == 5):
            quantidades_de_filmes = len(minha_lista_de_filmes)

            valor_total_a_pagar = quantidades_de_filmes * 10

            print("R$", valor_total_a_pagar)

        else:

            opcao = input("Deseja voltar para o início? (s/n)")
            if(opcao == 's'): 
                inicio()
                break
            if(opcao == 'n'):
                tela_inicio()
                break

def alugar(filme):

     while True:

        filmes_alugados = {}
        filmes_alugados['filme'] = filme
        
        lista = [elem['filme'] for elem in minha_lista_de_filmes] #verifica repetições por meio das chaves
        if filme in lista: #caso já esteja em uso, solicita um nome email
            print("O filme já foi alugado")
        else:
            minha_lista_de_filmes.append(filmes_alugados)
            print("Filme alugado com sucesso!\n")
        
        tela_inicio()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

inicio()

while True:

    opcao1 = int(input("Escolha uma das opções: "))

    while opcao1 > 6 or opcao1 < 0:
        opcao1 = int(input("Erro, tente novamente | Escolha uma opção: "))
       

    if(opcao1 == 1):
        cadastro()
    
    elif(opcao1 == 2):
        login()

    elif(opcao1 == 3):
        dadosUsuarios()

    elif(opcao1 == 4):
        mostrarUsuario()
    
    elif(opcao1 == 5):
        excluir_Usuario()

    else:
        print("Saindo...")
        break

