# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

V = float(input('informe o Valor do produto: '))
P = int(input('Informe a % de desconto que deseja aplicar: '))
desc = V - (V * (P / 100))
print(f'O valor final com desconto de {P}% será de {desc}R$')

