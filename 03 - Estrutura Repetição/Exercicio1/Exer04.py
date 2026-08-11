


contador = 0

while contador < 10:
    itens = int(input("Digite a Quantiade de Itens: "))

    if contador + itens > 10:
        print("Quantide excedeu o limite")
        break

    if itens < 0 or itens == 0:
        print("Quantidade Invalida!" )
        continue

    contador = contador + itens
    print(f'A Quantidae Acumulada foi de {contador}')


