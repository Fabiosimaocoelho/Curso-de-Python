# Exemplo sem lista
# nome1 = 'Fabio'
# nome2 = 'Jessica'
# nome3 = 'Francisco'
# nome4 = 'Irani'

# Exemplo com lista
# nomes = ['Jessica' , 'Fabio' , 'Franciso','Irani']

# Acessando valor na lista (Array)
# frutas = ['Banana', 'Uva','Maça','Manga']
# print(frutas[2])
# print(frutas[1])
# print(frutas[2]) # todos os valores de uma vez
# tamanho_array_frutas = len(frutas)
# print(f'No aray de frutas tem {tamanho_array_frutas} frutas')

# Paseando pelo array usando for
# carros = ['Gol' , 'Fusca', 'Brasilia','Opal']

# for i in carros:
#     print(f'Carr: {i}')

carrinho_compras = [150, 260, 100, 50, 60]
soma = 0

for i in carrinho_compras:
    soma = soma + i

print(f'A soma total dos produtos foi de R$ {soma},00')

