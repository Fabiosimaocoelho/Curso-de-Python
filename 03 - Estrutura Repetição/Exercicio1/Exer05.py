# Exercícios Práticos - While
# 1. O Caixa Eletrônico (Controle de Saldo e Validação)
# Contexto: Você está desenvolvendo o sistema básico de um caixa eletrônico.
# O cliente começa com um saldo inicial de R$ 500. Ele pode realizar sucessivos
# saques até que decida parar ou seu saldo acabe.
# Requisitos:
# Crie um loop 
# zero.
# while
#  que continue rodando enquanto o saldo for maior que
# A cada iteração, solicite ao usuário o valor que deseja sacar (ou 0
#  para
# encerrar o atendimento).
# Se o usuário digitar 0
# , use a instrução 
# break
#  para encerrar o loop
# imediatamente.
# Se o valor do saque for maior que o saldo disponível, exiba uma mensagem
# de erro e use 
# continue
#  para tentar uma nova operação sem descontar do
# saldo.
# Se o saque for válido, subtraia o valor do saldo e exiba o saldo restante.
# Use o bloco 
# else
#  no final do 
# while
#  para exibir uma mensagem quando o
# saldo zerar totalmente sem o uso do 
# break 
# .


# 2. Controle de Estoque com Validação de Quantidade
# Contexto: Uma loja precisa registrar a entrada de novos produtos no estoque
# através de um painel simples. O sistema deve aceitar a inclusão de itens um a
# um até atingir o limite máximo de 10 itens cadastrados na sessão.
# Requisitos:
# Inicialize uma variável 
# Escreva um loop 
# contador = 0 
# .
# while
#  que execute enquanto 
# contador < 10 
# .
# Em cada iteração, peça para o usuário digitar a quantidade de itens a
# adicionar ao lote.
# Se o usuário digitar um valor negativo ou igual a zero, exiba uma
# mensagem dizendo "Quantidade inválida!" e use a instrução 
# continue
#  para
# 1
# Exercícios Práticos - While
# repetir a tentativa sem incrementar o contador.
# A cada entrada válida, incremente a variável 
# contador
#  com a quantidade
# inserida e mostre o total acumulado até o momento.


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
