supersomador = [1, 6]
# supersomador = [15, 19]

def soma_lista(lista):
    soma = 1
    for i in lista:
        soma += i
    return soma

soma_supersomador = soma_lista(supersomador)
print(f'soma de todos valores {supersomador} ')


