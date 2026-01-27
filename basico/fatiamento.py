# Toda string é guardada como uma cadeia de caracteres, sendo possível fatia-la 

frase = 'Curso em Vídeo Python'

# Tal string tem 21 caracteres totais, contando o 0.

print(frase[9:14])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Análise de String

print(len(frase)) # mostra a quantidade de caracteres
print(frase.count('o')) # conta a quantidade de dado caracter
print(frase.count('o',0,13)) # conta a quantidade de dado caracter limitado 
print(frase.find('deo')) # ele procura aonde ocorre/começou
print(frase.find('Android')) # caso ele não encontre, retorna -1
print('Curso' in frase) # retorna true or false

# Transformação

frase.replace('Python','Android') # substitui a frase por outra
frase.upper() # deixa em maiúscula
frase.lower() # deixa em minúscula
frase.capitalize() # deixa somente o primeiro caracter em maiúsculo
frase.title() # deixa todo começo de palavra em maiúscula, o espaço delimita uma quebra de palavra
frase.strip() # remove todos os espaços inúteis do começo e final.
frase.rstrip() # remove só os espaços finais à direita
frase.lstrip() # remove o espaço da esquerda

# Divisão

frase.split() # separa as palavras em strings lista, cada elemento será uma palavra

# Junção

print(' '.join(frase))