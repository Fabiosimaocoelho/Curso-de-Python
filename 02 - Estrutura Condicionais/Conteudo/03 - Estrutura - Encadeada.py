# Permite varias condicoes
# nota = float(input('Digite sua nota: '))

# if nota >= 8:
#     print('Aprovado')
# elif nota >= 5:
#     print('Recuperacao')
# else:
#     print('Reprovado')

# print('         Exemplo        ')

# idade = int(input('Digite sua idade:'))

# if idade < 12:
#     print('Crianca')
# elif idade < 18:
#     print('Adolescente')
# elif idade < 60:
#     print('Adulto')
# else:
#     print('Melhor Idade')

print('         Exemplo        ')

usuario = input('Possui cadastro? (S/N): ').upper()
senha = input('Senha correta? (S/N): ').upper()

if usuario == 'S' and senha == 'S':
    print('Acesso liberado')
else:
    print('Acesso negado')