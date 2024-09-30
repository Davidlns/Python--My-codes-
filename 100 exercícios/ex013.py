#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

S = float(input('Informe Seu salário: '))
A15 = S + (S * (15 / 100))
print('Seu novo salário com aumento de 15% é de {}R$'.format(A15))