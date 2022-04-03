
def calculadora():
    print('\n','-' * 40, '\n         C A L C U L A D O R A', '\n', '-' * 40 )

def menu():
    calculadora()
    print('1. Somar'
          '\n2. Subtrair'
          '\n3. Multiplicar'
          '\n4. Dividir'
          '\n5. Digitar outros números'
          '\n6. Sair\n')

def somar(n1=0,n2=0):
    r = n1 + n2
    return r

def subtrair(n1=0,n2=0):
    r = n1 - n2
    return r

def multiplicar(n1=0,n2=0):
    r = n1 * n2
    return r

def dividir(n1=0,n2=0):
    r = n1 / n2
    return r

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

while n1 >= 0 or n2>=0:
    menu()
    opcao = int(input('Qual a sua opção?  [1/2/3/4/5/6]?'))

    if opcao < 1 or opcao > 6:
        print('\nOpção Inválida!\n')
        continue

    if opcao == 1:
        res = somar(n1,n2)
        print('{} + {} = {}'.format(n1,n2,res))

    elif opcao == 2:
        res = subtrair(n1,n2)
        print('{} - {} = {}'.format(n1,n2,res))

    elif opcao == 3:
        res = multiplicar(n1,n2)
        print('{} * {} = {}'.format(n1,n2,res))

    elif opcao == 4:
        res = dividir(n1,n2)
        print('{} / {} = {:.2f}'.format(n1,n2,res))

    elif opcao == 5:
        n1 = int(input('Número 1: '))
        n2 = int(input('Número 2: '))

    elif opcao == 6:
        break