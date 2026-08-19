# numeros = []

# valor_numeros = int(input('Favor informa numero:'))
# for i in range(valor_numeros):
#     digite = input('Qual numero?:')
#     numeros.append(numeros)


def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

valor = int(input('Favor informa numero:'))
print(par_ou_impar(25))
