import os
import json

class BancoCadastro:
    def __init__(self) -> None:

        self.dados = []

        self.usuario_logado = None

        self.filmes_alugados = {}

        self.carregar_usuarios()

    def add_usuario(self, nome, senha, email, login):
        usuario = {}
        usuario['nome'] = nome
        usuario['senha'] = senha
        usuario['email'] = email
        usuario['login'] = login


        lista = {i['email']: i for i in self.dados} #verifica repetições por meio das chaves
        while usuario['email'] in lista: #caso já esteja em uso, solicita um nome email
            usuario['email'] = input("E-mail já está sendo usado, digite outro E-mail: ")

        lista = {i['login']: i for i in self.dados}
        while usuario['login'] in lista:
            usuario['login'] = input("Login já está sendo usado, digite outro: ")
        
        self.dados.append(usuario)

        self.salvar_usuarios()

    def validar_login_usuario(self, login, senha):

        lista_login = {i['login']: i for i in self.dados} #verifica repetições por meio das chaves
        lista_senha = {i['senha']: i for i in self.dados} #verifica repetições por meio das chaves

        if login in lista_login and senha in lista_senha:
            return True
        
        return False

    def pegar_dados_usuario(self, login):
         lista_login = {i['login']: i for i in self.dados}

         if login in lista_login:
            return lista_login[login]
    
    def mostrar_dados_usuario(self):

        print("# Usuários cadastrados #")

        for i in self.dados:

            print('Nome:', i['nome'], 'Login: ', i['login'] )

    def exclusão_de_usuario(self, login, senha):

        for i in range(len(self.dados)):
            element = self.dados[i]
            if element["login"] == login and element["senha"] == senha:
                usuario_excluido = self.dados.pop(i)
                return usuario_excluido

        self.salvar_usuarios()

    def salvar_usuarios(self):
        with open("dados_usuarios", 'w') as f:
            json.dump(self.dados, f)
    
    def carregar_usuarios(self):
        
        if(os.path.exists("dados_usuarios")):
            with open("dados_usuarios", 'r') as f:
                self.dados = json.load(f)
    
    def buscar_filme(self, busca):

          for i in range(len(estoque_de_filmes)):
                filme = estoque_de_filmes[i]
                if filme == busca:
                    return filme
    
    def alugar_filme(self, filme, usuario):

        email_usuario = usuario['login']

        filmes_existentes = self.filmes_alugados.get(email_usuario, [])

        filmes_existentes.append(filme)

        self.filmes_alugados[email_usuario] = filmes_existentes

    def buscar_filme_do_usuario(self, usuario, filme):

        filmes_existentes = self.filmes_alugados.get(usuario['login'], [])

        if filme in filmes_existentes: #caso já esteja em uso, solicita um nome email
            return filme

    def calcular_valor_a_pagar_do_usuario(self, usuario):

        filmes_existentes = self.filmes_alugados.get(usuario['login'], [])

        quantidades_de_filmes = len(filmes_existentes)

        valor_total_a_pagar = quantidades_de_filmes * 10

        return valor_total_a_pagar
    
    def filmes_alugados_do_usuario(self, usuario):

         filmes_existentes = self.filmes_alugados.get(usuario['login'], [])
         return filmes_existentes


banco_Cadastro = BancoCadastro()
galeria_de_filmes = ['O poderoso chefão', 'O rei leão', 'O senhor dos anéis: o retorno do rei', 'À espera de um milagre', 'Vingadores: Ultimato', 'Batman - O cavaleiro das trevas', 'A vida é bela', 'O poderoso chefão 2', 'Vingadores: Guerra infinita', 'Viva -  A vida é uma festa', 'De volta para o futuro']
filmes_lancados_recentemente = ['Sorria', 'Uncharted: Fora do mapa', 'Órfã 2: A origem', 'Jurassic World', 'Top gun: Maverick', 'The Batman', 'Homem Aranha: Sem volta pra casa', 'Thor Amor e Trovão', 'Velozes e Furiosos 9', 'Terrifeir']
filmes_atualmente_reservados = []
minha_lista_de_filmes = []
estoque_de_filmes =  filmes_lancados_recentemente + galeria_de_filmes
usuario = None

def cadastro():

    while True:
        print("# Digite suas informações #")
        print("\n")
    

        nome = str(input("Digite seu nome: "))
        senha = input("Digite uma senha (Obs: contendo apenas números): ")
        email = input("Digite seu email: ")
        
        login = input("Digite seu login: ")
        
        banco_Cadastro.add_usuario(nome, senha, email, login)

        print("Cadastro realizado com sucesso!\n")

        opcao = input("Deseja realizar mais um cadastro? (s/n): ")
        if(opcao == 'n'): 
            inicio()
            break

def login():

    while True:

        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        if banco_Cadastro.validar_login_usuario(login, senha): 
            banco_Cadastro.usuario_logado = {
                "login":login
            }
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

        login = input("Login: ")

        dados_usuario = banco_Cadastro.pegar_dados_usuario(login)

        if dados_usuario != None:
            print(f"Dados dos usuário [{login}]: {dados_usuario}")
        else:
            print("Usuário não encontrado!")

        opcao = input("Deseja consultar outro usuário? (s/n)")
        if(opcao == 'n'): 
            inicio()
            break

def mostrarUsuario():

    while True:

        banco_Cadastro.mostrar_dados_usuario()
        
        opcao = input("Deseja consultar novamente? (s/n)")
        if(opcao == 'n'): 
            inicio()
            break

def excluir_Usuario():

    while True:
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
    
        usuario_excluido = banco_Cadastro.exclusão_de_usuario(login, senha)
    
        if(usuario_excluido != None):
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
            for i in banco_Cadastro.filmes_alugados_do_usuario(banco_Cadastro.usuario_logado):
                print(i)

        elif(opcao2 == 4):

            busca = input(print("Qual filme deseja buscar? "))
    
            filme_encontrado = banco_Cadastro.buscar_filme(busca)

            if(filme_encontrado != None):

                print("Filme encontrado!")

                opcao3 = input("Deseja alugar? (s/n)")
                if(opcao3 == 's'):
                    alugar(filme_encontrado)
                if(opcao3 == 'n'):
                    tela_inicio()

            if not filme_encontrado:
                print("Filme não encontrado!")
                tela_inicio()
                break

        elif(opcao2 == 5):
            
            valor_a_pagar = banco_Cadastro.calcular_valor_a_pagar_do_usuario(banco_Cadastro.usuario_logado)

            print("R$", valor_a_pagar)

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

        filme_alugado = banco_Cadastro.buscar_filme_do_usuario(banco_Cadastro.usuario_logado, filme)
        
        if (filme_alugado != None):
            print("O filme já foi alugado")
        else:
            banco_Cadastro.alugar_filme(filme, banco_Cadastro.usuario_logado)
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

