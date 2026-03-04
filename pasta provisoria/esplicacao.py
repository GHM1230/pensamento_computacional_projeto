'''
CRUD

print('Sistema de Agendamento de Aulas - Meet')
print('')
print(':: programação phyton:')
print('')
print('turma A segunda e quarta')
print('')
print('Turma A 8:00 - 12:00')
print('')
print('Turma A 10:00 - 12:00')

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