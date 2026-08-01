# Crie um programa que solicite o peso e altura e mostr o IMC da pessoa
nome = input('Qual seu nome? ')
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

imc = peso / altura **2
imc_perfeito = round(imc,2)

if imc < 18.5:
    print('Seu IMC é' , imc ,'Abaixo do peso normal')
elif imc >= 18.5 and imc  <= 24.9:
    print('Seu IMC é',imc, 'Peso normal')
elif imc >= 25.5 and imc <= 29.9:
    print('Seu IMC é',imc, 'Excesso de peso')
elif imc >= 30.0 and imc <= 34.9:
    print('Seu IMC é', imc,'Obsidade classe I')
elif imc >= 35.0 and imc <= 39.9:
    print('SeU IMC é', imc, 'Obsidade classe II')
else:
    print('Obsidade classe III:')

#imc_perfeito = round(imc,2)

