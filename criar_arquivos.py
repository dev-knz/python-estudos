import os

# pasta onde os arquivos serão criados
pasta = "beecrowd2"

# cria a pasta se não existir
os.makedirs(pasta, exist_ok=True)

conteudo = """# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
"""

for i in range(1000, 3349):
    nome_arquivo = f"{i}.py"
    caminho = os.path.join(pasta, nome_arquivo)
    
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)

print("Arquivos criados com sucesso!")