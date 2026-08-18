carrinho_compras = [30,70,48,95,85] + [150, 260, 100, 50, 60]
# precos = [40.25,21.89,100.85]
# idades = [35,45,23,90]

# com funcao
# carrinho_compras = [150, 260, 100, 50, 60]
def soma_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

soma_carrinho = soma_lista(carrinho_compras)
print (f'A soma carrinho compra foi de {soma_carrinho}')