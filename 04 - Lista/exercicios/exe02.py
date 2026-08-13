# Comece com uma lisata vazia 
# Com for adicione produtos em uma lista usando input() e append()
# E com outro for mostre os produtos cadastrados

produtos = []
# produtos.append('Arroz')
# produtos.append('Feijao')
# produtos.append('Macarrão')
# produtos.append('Alcatra')

# print(produtos)
# print(f'tipo de produtos: {len(produtos)}')

# print('=== Perguntar varias vezes algo ===')
# # nomes = ['Arroz' , 'Feijao' , 'Macarrao','Alcatra']

# for i in range(5):
#     print(f'Numero: {i}')
qtd_produtos = int(input('Quantos produtos voce vai cadastra? '))
for i in range(qtd_produtos):
    nome = input('Qual nome do produto? ')
    produtos.append(nome)

for i in produtos:
    print(f'nome: {i}')
