import time

def limpa():
    print('\n' * 4)

log = False # boolean para login

while not log:
    number = False # 1 número pelo menos
    upper = False # 1 letra maiúscula pelo menos
    low = False # 1 letra minúscula pelo menos

    print('Digite pelo menos 8 caracteres\nDigite pelo menos um número\nDigite pelo menos uma letra em maiúscula\nDigite pelo menos uma letra em minúscula')
    senha = str(input('Insira a senha: '))

    for letra in senha:
        if letra.isupper():
            upper = True
        elif letra.isdigit():
            number = True
        elif letra.islower():
            low = True
    
    if len(senha) >= 8 and upper and number and low:
            limpa()
            print('Senha forte!\nRegistrado com sucesso.')
            log = True
    
    else:
         limpa()
         time.sleep(1)
         print('Senha fraca!')
         if len(senha) < 8:
            time.sleep(1)
            print('Não há 8 caracteres totais.')
         if not upper:
            time.sleep(1)
            print('Não há um caracter em maiúsculo.')
         if not low:
            time.sleep(1)
            print('Não há um caracter minúsculo.')
         if not number:
            time.sleep(1)
            print('Não há um dígito na senha.')
         time.sleep(3)
         limpa()

    