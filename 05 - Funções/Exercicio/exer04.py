# supersomador = [1, 6]
# supersomador = [15, 19]

def super_somador(inicio,fim):
    soma = 0
    for i in range(inicio,fim + 1):
        soma += i

    return soma

print(super_somador(1,6))
print(super_somador(15,19))