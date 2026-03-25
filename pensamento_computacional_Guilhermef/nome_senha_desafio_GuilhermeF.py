'''
print("Bem-vindo ao sistema de login!")
print("Por favor, insira o que é pedido:")
usuario = input("Digite seu nome: ")
senha = input("Digite sua senha: ")


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


# Definimos a função para organizar o processo de login
def realizar_login():
    """
    Função que simula uma tela de login capturando nome e senha.
    """
    print('\n--- Tela de login - Meet ---')
    
    # Captura de dados (como no teu exemplo original)
    nome_usuario = input('Digite seu login para continuar: ')
    senha_usuario = input('Digite sua senha para continuar: ')
    
    # Exibe a mensagem de sucesso
    print(f'Bem-vindo, {nome_usuario}!')
    print('---------------------------\n')

# Agora, para o código funcionar, precisamos "CHAMAR" a função:
realizar_login()

'''

import getpass 

def realizar_login_com_tentativas():

    senha_padrao = "vocacao2025"
    tentativas_restantes = 3
    login_sucesso = False
    
    
    print('\n--- Sistema de Login (máximo de 3 tentativas) ---')
    nome_usuario = input('Digite seu login: ')
    
    while tentativas_restantes > 0 and not login_sucesso:
        print(f'\nTentativas restantes: {tentativas_restantes}')
        senha_digitada = getpass.getpass('Digite sua senha (os caracteres não aparecerão): ')

        if senha_digitada == senha_padrao:
            print(f'\n[SUCESSO] Bem-vindo, {nome_usuario}!')
            login_sucesso = True

        else:
            tentativas_restantes -= 1
            if tentativas_restantes > 0:
                print('\n[ERRO] Senha incorreta! Tente novamente.')
            else:
                print('\n[BLOQUEADO] número de tentativas excedido!')

    print(f'\n --- fim da operação --- \n')

realizar_login_com_tentativas()