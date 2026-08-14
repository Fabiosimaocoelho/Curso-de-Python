# Exercício: Números e seus
# quadrados
# Crie um programa que peça ao usuário 5 números inteiros.
# O programa deve:
# Criar uma lista vazia chamada 
# quadrados 
# .
# Usar um 
# for
#  para pedir os 5 números.
# Calcular o quadrado de cada número.
# Adicionar o resultado na lista usando 
# append() 
# .
# No final, mostrar todos os quadrados calculados.
# Exemplo:
# Digite um número: 2
# Digite um número: 5
# Digite um número: 3
# Digite um número: 10
# Digite um número: 4
# Quadrados:
# 4
# 25
# 9
# 100
# 16
# Desafio: no final, calcular e mostrar a soma de todos os quadrados.
# Soma dos quadrados: 154
# Aqui eles praticam 
# for 
# , 

quadrados = []
soma_quadrados = 0

for i in range(5):
    numero = int(input('Qual numero?: '))
    quadrado = numero **2
    quadrados.append(quadrado)

for i in quadrados:
    print(i)
    soma_quadrados = soma_quadrados * 1

print(f'quadrados: {i}')
