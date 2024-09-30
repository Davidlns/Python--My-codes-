#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

TC = float(input('Informe a Temperatura em C: '))
TF = (TC * 9 / 5) + 32

print(f'{TC}°C convertendo fica {TF}°F em Fahrenheit')
