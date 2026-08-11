
# 3. Jogo da Adivinhação com Tentativas Limitadas
# Contexto: Em um minigame, o jogador precisa adivinhar um número secreto
# entre 1 e 20. O jogador tem no máximo 5 tentativas para acertar.
# Requisitos:
# Defina uma variável com o número secreto (por exemplo, 
# 14 
# ) e outra para contar as tentativas (
# O loop 
# while
#  deve continuar enquanto 
# Peça para o jogador chutar um número.
# break
#  para encerrar o jogo.
# numero_secreto = 
# tentativas = 1 
# ).
# tentativas <= 5 
# .
# Se o jogador acertar o número secreto, exiba uma mensagem de parabéns
# e use 
# Se o chute estiver incorreto, informe se o número secreto é maior ou 
# menor que o palpite e incremente o contador de tentativas.
# Utilize a cláusula 
# else
#  vinculada ao 
# while
#  para exibir a mensagem de
# "Game Over! Suas tentativas acabaram." caso o jogador não consiga
# acertar dentro das 5 chances.

import random

numero_secreto = random.randint(1,150)
tentativas = 5

print("=== Voce Tera Cinco Tentativas  ===")
while tentativas >= 0:
    chute = int(input("Numero Secreto entre 1 e 150: "))

    # tentativas +=1
    if chute == numero_secreto:
        print("Parabéns, voce acertou! ")
        break

    if chute > numero_secreto:
        print('Numero Secreto é menor')
    else:
        print('Numero Secreto é maior')

    tentativas -= 1
    print(f'Voce tem {tentativas} tentativas')
else:
    print('GAME OVERRRRRR - NOOB')


   


    


    
