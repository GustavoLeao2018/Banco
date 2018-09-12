from trabalho.Banco import *
from random import choice, randint
from trabalho.Guis import *


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
    print("="*100)
    for item in lista:
        print(item)
    print("="*100)

def alterar(db):
    quantidade = db.ler_quantidade()
    db.editar_produto((randint(0, quantidade), randint(0, 100)))
    ler(db)

def deletar(db):
    quantidade = db.ler_quantidade()
    db.apagar_produto((randint(0, quantidade),))
    ler(db)

if __name__ == '__main__':
    db = Banco()
    for i in range(0, 15):
        p = produto()
        db.inserir_produto(p)
    ler(db)
    deletar(db)
    alterar(db)

    g = Guis()
    g.inserir()

