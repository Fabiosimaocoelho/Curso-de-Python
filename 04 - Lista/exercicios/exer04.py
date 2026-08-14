# Para descubrir se um numero é par ou impar
# % ------------- modulo
# if 10 % 2 == 0:
#     print('par')
# else:
#        print('impar')

# Peca o usuario para cadastrar numeros em uma lista
# Conte quantos impares e pares tem nessa lista 

lista = []
impares = 0
pares = 0

for i in range(6):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

    if i % 2 == 0:
        pares = pares + 1
        # print("Par")
    else:
        # print('Impar')
        impares += 1


# numeros = []

# qtd_numeros = int(input('Favor informa quantidade:'))
# for i in range(qtd_numeros):
#     digite = input('Qual numero?:')
#     numeros.append(numeros)

# if 8 % 2 == 0:
#     print('lista par')

# else:
#     print('impar')
