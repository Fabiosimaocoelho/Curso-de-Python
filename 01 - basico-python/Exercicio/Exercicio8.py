

vip = input('Cliente Vip: (S/N)')
valor = float(input('Valor da compra: '))

participa_promocao = (vip == 'S' or vip == 's') or valor > 500


print(                      )
print(f'Cliente participar da promocao: {participa_promocao}')
