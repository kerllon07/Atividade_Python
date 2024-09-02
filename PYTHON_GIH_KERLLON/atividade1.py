#Ordenação natural

numeros = [5,2,9,1,5,9]
print(numeros)

#Ordenação customizada


pessoas = [
    {"nome": "João", "idade": 25},
    {"nome": "Maria", "idade": 22},
    {"nome": "Ana", "idade": 25},
    {"nome": "Carlos", "idade": 30},
]

ordenacao_customizada_pessoas = sorted(pessoas, key=lambda x: (x["idade"], x["nome"].lower()))
print("Ordenação Customizada (por idade e depois por nome):")
for pessoa in ordenacao_customizada_pessoas:
    print(pessoa)