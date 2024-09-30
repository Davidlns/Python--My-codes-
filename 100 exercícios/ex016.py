#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
from math import floor

numr = float(input('Digite um valor real: '))

print(f'A porção inteira do número {numr} é igual a {floor(numr)}')