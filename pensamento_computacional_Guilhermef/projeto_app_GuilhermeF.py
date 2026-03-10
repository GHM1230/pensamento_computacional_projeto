'''

CRUD

AÇAÍTERIA

descrição

'''

print("\n=== 🍷 Açaíataria 🍷 ===\n")

print("1. Cadastro 📝 ")
print("2. Cardápio 📋")
print("3. Pedidos 🛒")
print("4. Feedback 🗣️")
print("5. Ajuda ❓")
print("0. Sair 🚪")

while True:

    escolha_menu = input("\nEscolha uma opção: ")
    if escolha_menu == "1":

        print("Agendando cadastro...")
        nome_cliente = input("Digite o nome do cliente: ")
        telefone_cliente = input("Digite o telefone do cliente: ")
    
    elif escolha_menu == "0":
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")

'''

CRUD
    
sistema de agendamento de aulas - meet

'''
print("sistema de agendamento de aulas - meet")

id_usuario = input(" Seja bem-vindo! Por favor, insira seu nome para continuar: ")

print("\n" + "_" * 15)

aluno_turma = input ('digite sua turma: (ex: A, B, C, D ): ')

email_usuario = input('Digite seu email: (nome.sobrenome@gmail.com) ')

print('')
print(':: programação phyton:')
print('')
print('turma A segunda e quarta')
print('')
print('Turma A 8:00 - 12:00')
print('')
print('Turma A 10:00 - 12:00')

'''

CRUD

calculadora simples - Python Vocação

'''

print('\n Calculadora simples - Python Vocação \n')

number_um = input('digite o primeiro número :')
number_dois = input('digite o segundo número :')

operar_number = input('Escolha a operacao: 1 -> +, 2 -> -, 3 -> *, 4 -> /')

if operar_number == '4':
    result = int(number_um) / int(number_dois)
    print(f'O resultado é: {result}')

elif operar_number == '3':
    result = int(number_um) * int(number_dois)
    print(f'O resultado é: {result}')

elif operar_number == '2':
    result = int(number_um) - int(number_dois)
    print(f'O resultado é: {result}')

elif operar_number == '1':
    result = int(number_um) + int(number_dois)
    print(f'O resultado é: {result}')

else:
    print('número não divido por zero.')