# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico

def leiaint(msg):
    num = str(input(msg))
    while True:
        try:
            num = int(num)
            break
            return num
        except:
            num = str(input('ERRO! Digite um número inteiro válido '))

n = leiaint('Digite um número ')
