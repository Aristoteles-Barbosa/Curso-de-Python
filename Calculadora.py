print('*******************Calculadora em Python*******************')

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multyply(x,y):
    return x * y

def divide(x,y):
    return x / y

print('Digite as opções abaixo')
print ('1 - Soma')
print ('2 - Subtração')
print ('3 - Multiplicação')
print ('4 - Divisão')

opcao = input('Digite a opção (1/2/3/4): ')

num1 = int(input('\n Digite o primeiro numero: '))

num2 = int(input('\n Digite o segundo numero: '))

if opcao == '1':
    print('\n')
    print(num1, "+", num2, "=", add(num1,num2))
    print('\n')

elif opcao == '2':
    print('\n')
    print(num1, "-", num2, "=", subtract(num1,num2))
    print('\n')

elif opcao == '3':
    print('\n')
    print(num1, "*", num2, "=", multyply(num1,num2))
    print('\n')

elif opcao == '4':
    print('\n')
    print(num1, "/", num2, "=", divide(num1,num2))
    print('\n')

else:
    print('Opção Inválida')