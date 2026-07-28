# Entrada
# nome = 'Fabio Simao Coelho'
# idade = 44
# cidade = 'Vitória' 
# altura = 1.70
# print('Eu',nome,'tenho',idade,'moro',cidade,'tenho autura',altura,'possui carteira motorista')
# carteira = True

# Saida
# nome = 'Fabio Simao Coelho'
# Idade = 44
# cidade = 'Vitoria'
# Altura = 1.70
# print('Eu',nome,'tenho',idade,'Moro',cidade,'Altura',altura,'Possui carteira de motorista')
# carteira = True

Nome = input("Qual seu nome? ")
Idade = int(input('Qual sua idade '))
Cidade = input("Qual sua cidade? ")
Altura = float(input('Qual sua altura: '))
Carteira = input("Possui carteira de motorista? (S/N) ")
possui_carteira = Carteira == 'S' or Carteira =='s'

print('--- Dados do Uusuario ---')

print(f'Nome: {Nome}')
print(f'Idade: {Idade}')
print(f'Cidade: {Cidade}')
print(f'Altura: {Altura}')
print(f'Possui carteira de motoriasta: {possui_carteira}')

nome_produto = input('Digite o nome do produto: ')
preco_produto = float(input('Digite o preço: '))
Quantidade_disponivel_produto = int(input('Digite a quantidade disponível: ')) 
Categoria_produto = input('Digite a categoria: ') 
Promocao_produto = input("O produto esta em promoção? (S/N) ")

print(f'Nome_produto: {nome_produto}')
print(f'preco_produto: {preco_produto}')
print(f'Quantidade_disponivel_produto: {Quantidade_disponivel_produto}')
print(f'Categoria_produto: {Categoria_produto}')
print(f'Promocao_produto: {Promocao_produto}')
Promocao = False


