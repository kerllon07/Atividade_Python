import re

def natural_key(string):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', string)]

def natural_sort(lst):
    return sorted(lst, key=natural_key)

# Lista de strings com números
lista = ["item3", "item2", "item10", "item4", "item5"]

# Ordenação natural
lista_ordenada = natural_sort(lista)

print("Lista ordenada:", lista_ordenada)