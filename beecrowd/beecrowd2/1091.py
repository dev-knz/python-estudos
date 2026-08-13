m = int(input())
soma = 0
for i in range(1, m+1):
    if i <= 2:
        soma += 1
    
    elif i == 3:
        soma += 2
        
        # Definindo o ultimo e penultimo digito pela lógica
        ultimo = 1
        penultimo = 2
        
    else:
        # Uso um auxiliador para guardar o penultimo
        aux = penultimo
        
        # Penultimo soma com o ultimo
        penultimo += ultimo
        
        # E esse resultado de cima eu uso na minha soma
        # Guardo o ultimo digito com o aux, que é a copia do penultimo
        ultimo = aux
        soma += penultimo
print(soma)
        

