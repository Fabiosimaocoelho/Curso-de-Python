def media_nota(n1,n2,n3):
    media =(n1+n2+n3)/3
    return media

nota1 = float(input('Digite a 1º: ')) # 5
nota2 = float(input('Digite a 2º: ')) # 6
nota3 = float(input('Digite a 3º: ')) # 7

media = media_nota(nota1,nota2,nota3)
print(media)

def situacao_aluno(media):
    if media >=7:
        return 'Aprovado'
    elif media >= 5 and media <= 6.9:
        return 'Recuperacao'
    else:
        return 'Reprovado'
resultado = situacao_aluno(media)

print(resultado)