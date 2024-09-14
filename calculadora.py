import math
import time
import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def adição(a, b):
    return a + b

def subtração(a, b):
    return a - b

def multiplicação(a, b):
    return a * b

def divisão(a, b):
    if b != 0:
        return a / b
    else:
        print('ERRO: DIVISÃO POR 0')

def raiz_quadrada(a, b):
    firstorsecond = int(input(('Deseja a raiz quadrada do número 1 ou 2? ')))

    if firstorsecond == 1:
        if a < 0:
            print('ERRO: RAIZ QUADRADA DE UM NÚMERO NEGATIVO')

        else:
            return print(f'A raiz quadrada de {a} é ', math.sqrt(a))
        
    elif firstorsecond == 2:
        if b < 0:
            print('ERRO: RAIZ QUADRADA DE UM NÚMERO NEGATIVO')

        else:
            return print(f'A raiz quadrada de {b} é ', math.sqrt(b))

    else:
        print('Comando Invalido')

def potenciação(a, b):
    potfirstorsecond = int(input('Deseja potenciar o número 1 ou 2? '))
    if potfirstorsecond == 1:
        expoente = int(input(f'Elevar {a} a qual expoente? '))
        if expoente < 0 and a == 0:
            print('ERRO: INDEFINIDO')
        elif expoente == 0 and a == 0:
            print('ERRO: INDEFINIDO')
        else:
            return print(f'{a} elevado a {expoente} é', math.pow(a, expoente))
    elif potfirstorsecond == 2:
        expoente = int(input(f'Elevar {b} a qual expoente? '))
        if expoente < 0 and b == 0:
            print('ERRO: INDEFINIDO')
        elif expoente == 0 and b == 0:
            print('ERRO: INDEFINIDO')
        else:
            return print(f'{b} elevado a {expoente} é', math.pow(b, expoente))

while True:
    print('-' * 20, 'CALCULADORA', '-' * 20)
    print('Escolha o número da operação: ')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Raiz Quadrada')
    print('6 - Potenciação')
    print('7 - Sair')

    escolha = int(input('Número da operação: '))

    if escolha == 7:
        print('Saindo...')
        time.sleep(0.75)
        limpar_tela()
        break

    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))

    if escolha == 1:
        print(f'Resultado: {adição(num1, num2)}')
    elif escolha == 2:
        print(f'Resultado: {subtração(num1, num2)}')
    elif escolha == 3:
        print(f'Resultado: {multiplicação(num1, num2)}')
    elif escolha == 4:
        print(f'Resultado: {divisão(num1, num2)}')
    elif escolha == 5:
        raiz_quadrada(num1, num2)
    elif escolha == 6:
        potenciação(num1, num2)

    continuar = input('Deseja continuar? (S/N) ').strip().lower()

    if continuar in ['s', 'sim']:
        limpar_tela()
        time.sleep(1.0)
        continue
    elif continuar in ['n', 'não', 'nao']:
        print('Saindo...')
        time.sleep(0.75)
        limpar_tela()
        break