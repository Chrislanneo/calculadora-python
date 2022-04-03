
def calculadora():
    print('\n','-' * 40, '\n         C A L C U L A D O R A', '\n', '-' * 40 )

def menu():
    calculadora()
    print(f"{'M E N U': ^40}")
    print('1. Somar'
          '\n2. Subtrair'
          '\n3. Multiplicar'
          '\n4. Dividir'
          '\n5. Porcentagem'
          '\n6. Potência'
          '\n7. Digitar outros números'
          '\n8. Sair\n')

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

def porcentagem(n1=0,n2=0):
    r = n1 * n2 /100
    return r

def potencia(n1=0, n2=0):
    r = n1 ** n2
    return r

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

while n1 >= 0 or n2>=0:
    menu()
    opcao = int(input('Qual operação realizar?  [1/2/3/4/5/6/7/8]?\n'))

    if opcao < 1 or opcao > 8:
        print('\nOpção Inválida!\n')
        continue

    if opcao == 1:
        res = somar(n1,n2)
        print('SOMA\n{} + {} = {}'.format(n1,n2,res))

    elif opcao == 2:
        res = subtrair(n1,n2)
        print('SUBTRAÇÃO\n{} - {} = {}'.format(n1,n2,res))

    elif opcao == 3:
        res = multiplicar(n1,n2)
        print('MULTIPLICAÇÃO\n{} * {} = {}'.format(n1,n2,res))

    elif opcao == 4:
        res = dividir(n1,n2)
        print('DIVISÃO\n{} / {} = {:.2f}'.format(n1,n2,res))

    elif opcao == 5:
        res = porcentagem(n1,n2)
        print('PORCENTAGEM\n{} % {} = {:.2f}'.format(n1,n2,res))

    elif opcao == 6:
        res = potencia(n1,n2)
        print('POTÊNCIA\n{} ^ {} = {:.2f}'.format(n1,n2,res))

    elif opcao == 7:
        n1 = int(input('Número 1: '))
        n2 = int(input('Número 2: '))

    elif opcao == 8:
        print('Bye!')
        break