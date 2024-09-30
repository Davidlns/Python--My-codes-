# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
try:
    lata = float(2)
    larg = float(input('Informe a largura da parede que deseja pintar: '))
    alt = float(input('Informe a altura da parede que deseja pintar: '))
    area = larg * alt
    print(f'\nSua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m²')

    calclatas = area / lata
    print(f'\n Você precisará de {calclatas} latas de tinta')
except:
    print("Favor reiniciar o programa, Digite somente numeros, em caso de numeros reais ultilize o ponto e não a virgula!")

