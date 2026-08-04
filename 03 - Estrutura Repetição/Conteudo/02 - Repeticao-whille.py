# # WHILE --------------- Enquanto
# # Contador = 1
# # While contador <= 8:     condicoes=True
# #    print('contador')
# #    contador = contador + 1
# #    contador += 1

# contador = 1

# print('=== incremento ===')
# while contador <= 8:
#     print(contador)
#     contador += 1 # incremento (adicionando +1)

# # decremento
# print('=== decremento ===')
# contador2 = 9

# while contador2 >= 1:
#     print(contador2)
#     contador2 -= 1

# # Interrupcao,
# print('=== Interrupcao ===')
# i = 1
# while i <= 12:
#     print(i)
#     if i == 10:
#         break
#     i += 1

# # Continue
# print('=== Continue ===')

e = 1
while e < 10:
    e += 1
    if e == 4:
        continue
    print(e)

# else
print('=== Else ===')
r = 1
while r < 6:
    print(r)
    r += 1
else:
    print('Condição deu Falos')