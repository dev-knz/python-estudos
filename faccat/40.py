number = ['PHP', 'Exercises', 'Backend', 'Python']

maior = 0
palavra = None

for i in number:
    if len(i) > maior:
        maior = len(i)
        palavra = i

print(f'A maior palavra é {palavra} com {maior} caracteres')