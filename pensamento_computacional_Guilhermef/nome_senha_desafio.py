'''
print("Bem-vindo ao sistema de login!")
print("Por favor, insira o que é pedido:")
usuario = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

'''
import getpass

def realizar_login():
    
    senha_padrao = "1234"
    
    print("\nBem-vindo ao sistema de login!\n")

    nome_usuario = input("Digite seu nome: ")

    senha_usuario = getpass.getpass('Digite sua senha (os caracteres não aparecerão): ')

    if senha_usuario == senha_padrao:
        print(f"\nBem-vindo, {nome_usuario}! Acesso concedido.\n")
    else:
        print("\nSenha incorreta. Acesso negado.\n")
    print('----------------------------------\n')

realizar_login()