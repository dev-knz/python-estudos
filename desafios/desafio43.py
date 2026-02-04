# Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

p = float(input('Insira o seu peso em kg: '))
h = float(input('Insira a sua altura em metros: '))

imc = p/(h**2)

if imc < 18.6:
    print('Abaixo do peso')
elif 18.4 < imc < 25.1:
    print('Peso ideal')
elif 24.9 < imc < 30.1:
    print('Sobrepeso')
elif 29.9 < imc < 40.1:
    print('Obesidade')
else:
    print('Obesidade mórbida')