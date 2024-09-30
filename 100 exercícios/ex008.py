# Escreva um programa que leia um valor em metros e converta em centímetros e milímetros

met = float(input('Escreva o valor em metros que deseja converter:'))
cent = met * 100
mil = met * 1000

print(f'\nMetros: {met} \nCentímetros: {cent} \nMilímetros: {mil} ')

# print(f'\nMetros: {met} \nCentímetros: {met * 100} \nMilímetros: {met * 1000} ') para não usar variável, caso não seja necessário
