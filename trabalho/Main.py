from trabalho.Banco import *
from random import choice, randint


produto_lista = [
    "Arroz","Feijão","Açúcar","Café","Chá","Achocolatado","Leite", "Pão","Farinha de Trigo", "Farinha de Rosca", "Amido de Milho",
    "Fermento"
]
tipo_lista = [
    "Comida"
]
preco_lista = [randint(100, 999) / 100.00 for x in range(10, 100)]
quantidade_lista = [randint(0, 100) for x in range(10, 100)]

def produto():
    produto = choice(produto_lista)
    tipo = choice(tipo_lista)
    preco = choice(preco_lista)
    quantidade = choice(quantidade_lista)

    return(produto, tipo, preco, quantidade)

def ler(db):
    lista = db.ler_produtos()
    print(lista)

if __name__ == '__main__':
    db = Banco()
    for i in range(0, 15):
        p = produto()
        db.inserir_produto(p)
    ler(db)