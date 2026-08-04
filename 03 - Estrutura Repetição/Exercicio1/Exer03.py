
# saldo = 10
# while saldo <= 10:
#     print(saldo)
#     saldo += 1
# saldo = 10

# i = 10
# while i <= 10:
#     print(i)
#     if i == 10:
#         break
#     i += 10

# e = 10
# while e < 10:
#     e += 1
#     if e == 10:
#         continue
#     print(e)

# r = 10
# while r < 10:
#     print(r)
#     r += 10

# else:
#     print('Saldo em conta 0')

Saldo_inicial = 500

print(f'Saldo inicial: R$ {Saldo_inicial:.2f}')

while Saldo_inicial > 0:
    valor_saque = int(input('Você deseja sacar quanto?:'))
    if valor_saque <= Saldo_inicial:
        Saldo_inicial -= valor_saque
        print(f'saldo atual: R$ {Saldo_inicial:.2f}')
    continue
else:
    print('Saldo Negativo')