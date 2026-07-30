# Regra:
# A soma de dois lados deve ser maior que o terceiro.
# Depois:
# Se os três lados forem iguais 

# lado1 = (input('Triângulo Equilátero: '))
# lado2 = (input('Triângulo Isósceles: '))
# lado3 = (input('Triângulo Escaleno: '))

# def equilatero(n):
#     for i in range(1, n + 1):
#         print(' ' * (n - i) + '*' * (2 * i - 1))

# def isosceles(n):
#     for i in range(1, n - 1):
#         print('*' * i)

# def escaleno(n):
#     for i in range(1, n+1):
#         print(' ' * (n -1) + '*' *1)

# print("equilatero:")
# equilatero (5)

# print("\ninsósceles:")
# isosceles(5)

lado1 = int(input('Lado1: '))
lado2 = int(input('Lado2: '))
lado3 = int(input('Lado3: '))

if (lado1 + lado2 > lado3) and (lado3 + lado2 > lado1) and (lado1 + lado3 > lado2):
    print('E um triangulo\n')

    if (lado1 == lado2 == lado3):
        print('Equilatero')
    elif (lado1 == lado2) or (lado1 == lado3) or(lado3 == lado2):
        print('isosceles')
    else:
        print('Escaleno')

else:
    print('Os valores informados não formam um triângulo')


              
