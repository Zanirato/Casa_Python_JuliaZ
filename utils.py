# Segujnda página criada
# Importa o módulo do tkinter para recursos extras de interface
import tkinter as tk

# Importa o método para abrir conexões com o banco de dados
from db import getconnection

def gerarcodigo():
    # Usa o banco de dados para determinar o último código usado e gerar o próximo
    with getconnection() as conn:
        # Busca o id mais alto da tabela de comidas
        cur = conn.execute("SELECT id FROM comidas ORDER BY id DESC LIMIT 1")
        row = cur.fetchone()
        # SE não houver cadastros, retorna o primeiro código padrão
        if not row:
            return "C001"
        # Gera o próximo código baseado no maior id atual
        # f"C{...:03d}" formata o número com 3 dígitos, preenchendo com zeros à esquerda
        return f"C{row['id'] + 1:03d}"
    
def mergesortproducts(products,key="nome"):
    """
    Ordena lista de comidas por atributo escolhido.
    Utiliza o algoritmo mergesort para garantir ordenação estável, eficiente e insensível a maiúsculas/minúsculas.
    """
    if len(products) <= 1:
        # Lista de tamanho <=1 já está ordenada
        return products
    
    mid = len(products) // 2
    left = mergesortproducts(products[:mid], key)
    right = mergesortproducts(products[mid:], key)

    merget = []
    i = j = 0
    # Faz a mesclagem dos blocos ordenados
    while i < len(left) and j < len(right):
        if str(left[i][key]).lower() < str(right[j][key]).lower():
            merget.append(left[i])
            i += 1
        else:
            merget.append(right[j])
            j += 1
    
    # Junta o que restou de cada metade (se sobrar)
    merget.extend(left[i:])
    merget.extend(right[j:])
    # Retorna a lista ordenada
    return merget

def centralizarjanela(win, largura=800, altura=600):
    # Centraliza a janela na tela do usuário
    win.update_idletasks() # Atualiza "idle" para pegar medidas corretas
    screenw = win.winfo_screenwidth()
    screenh = win.winfo_screenheight()
    x = screenw // 2 - largura // 2
    y = screenh // 2 - altura // 2
    win.geometry(f"{largura}x{altura}+{x}+{y}")  # Define posição e tamanho da janela
