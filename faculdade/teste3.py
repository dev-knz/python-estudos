contador = 0
logado = False

while contador != 3 and not logado:

    name = str(input('Insira o username: ')).strip()
    password = str(input('Insira a senha: ')).strip()

    if name == 'admin' and password == '1234':
        print('Acesso permitido. Bem-vindo, admin!')
        logado = True
    else:
        print('Usuário ou senha incorretos.')
        contador += 1

        if contador == 3:
            print('Conta Bloqueada.')