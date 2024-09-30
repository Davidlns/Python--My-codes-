# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo, calcule e mostre o comprimento da hipotenusa

from math import pow, sqrt

co = float(input('Informe o comprimento do Cateto Oposto: '))
ca = float(input('Informe o comprimento do cateto Adjacente: '))

hipo = float(sqrt( pow(co,2) + pow(ca,2) ))

print('O comprimento da Hipotenusa é igual a {:.2f}'.format(hipo))