
# Passo 5: Repetir o passo 4 até acabar a lista de produtos

# Para isso, vamos usar a biblioteca do pyautogui
# pip install pyautogui | No linux, crie um venv para o projeto

import pyautogui
import time
import pandas

# Entre cada comando, ele vai levar x segundos para executar
pyautogui.PAUSE = 0.3

# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)

# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa

# Abriria o navegador
pyautogui.press('win') # Aperta o botão windows
pyautogui.write('brave') # Escreve 'brave' 
pyautogui.press('enter') # Aperta o botão enter

pyautogui.write('link do website') # Escreve o site
pyautogui.press('enter') # Entra na página do site
time.sleep(5) # Dá uma pausa para o site carregar
# Recomendado assistir o vídeo do pyautogui | hashtag

# Passo 2: Fazer o login
pyautogui.click(x, y) # Use o auxiliar para pegar a posição
pyautogui.write('email') # Escreve o email

pyautogui.press('tab') # Passa para o próximo campo
pyautogui.write('senha') # Escreve a senha

pyautogui.press('tab') # Passa para o botão
pyautogui.press('enter') # Aperta o enter
time.sleep(3)

# Passo 3: Abrir a base de dados
# pip install pandas openpyxl # import pandas

tabela = pandas.read_csv('produtos.csv') # Guarda na memória 

# Passo 4: Cadastrar um produto

for linha in tabela.index:
    # Poderia ser também coluna in tabela.colums
    # Pegar a posição do primeiro campo com arquivo auxiliar.py

    # codigo
    pyautogui.click(x, y) # Clica no campo do código

    # loc[]
    codigo = tabela.loc[linha, 'codigo']

    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # marca
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    # tipo
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    # categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    # preco
    pyautogui.write(str(tabela.loc[linha, 'preco']))
    pyautogui.press('tab')

    # custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    # obs
    pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)