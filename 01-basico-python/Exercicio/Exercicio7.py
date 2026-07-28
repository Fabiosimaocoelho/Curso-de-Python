

cadastro = input('Usuario possui cadastro? (S/N) ')
senha = input('Senha está correta: (S/n) ')
validacao = (cadastro == 'S' or cadastro == 's') and (senha == 'S' or senha == 's')

print('---------------------------')
print(f'Resultado da validação: {validacao}')

