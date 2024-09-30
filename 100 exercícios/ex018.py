# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan

ang = int(input('Digite o ângulo: '))

r = radians(ang)

sen = sin(r)
co = cos(r)
tag = tan(r)

print('Usando o angulo de {}° graus, obtemos as seguintes medidas: \n Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}'.format(ang,sen,co,tag))