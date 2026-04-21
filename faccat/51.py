
lista = list()
dicionario = dict()
num = int(input('Digite quantas vezes você quer realizar o processo de cadastro: '))
 
for i in range(num):
    
    dicionario['nome'] = str(input('Insira o nome: ')).upper()
    dicionario['idade'] = int(input('Insira a sua idade: '))
    dicionario['sexo'] = str(input('Insira o gênero: ')).upper()

    lista.append(dicionario.copy())
    dicionario.clear()
print(lista)

