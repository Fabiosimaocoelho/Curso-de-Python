# Para criar uma fincao com retorno
def soma (a, b):
    return a + b

# Funcao com retorno, podemos colocar dentro de uma variavel 
total = soma(10,30) # - Argumento
print(f'O total da soma foi de: {total}')

# Saudacao
def saudacao(nome):
    return f"Ola seja bem vindo(a) {nome}"

mensagem = saudacao ('Fabio')
print(mensagem)

    