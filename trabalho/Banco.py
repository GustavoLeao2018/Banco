#!/bin/env python3
"""Banco de dados de um estoque."""
from sqlite3 import *


class Banco:
    def conectar(self):
        return connect("banco.db")
    def fechar(self, db):
        db.close()

    def tabela(self):
        sql = """
            CREATE TABLE IF NOT EXISTS produto(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                preco_unitario REAL NOT NULL,
                produto TEXT NOT NULL,
                quantidade INTEGER NOT NULL
            );
        """
        self.db = self.conectar()
        self.cursor = self.db.cursor()
        self.cursor.execute(sql)
        self.fechar(self.db)

    def inserir_produto(self, *args):
        sql = "INSERT INTO produto (produto, tipo, preco_unitario, quantidade) VALUES (?, ?, ?, ?);"
        self.db = self.conectar()
        self.cursor = self.db.cursor()
        self.cursor.execute(sql, *args)
        self.db.commit()
        self.fechar(self.db)

    def ler_produtos(self):
        sql = "SELECT * FROM produto;"
        self.db = self.conectar()
        self.cursor = self.db.cursor()
        self.produtos = self.cursor.execute(sql)
        self.lista_produtos = []

        for item in self.produtos.fetchall():
            self.lista_produtos.append(item)

        self.fechar(self.db)

        return self.lista_produtos

    def apagar_produto(self):
        sql = "DELETE FROM produto WHERE ;"

    def __init__(self):
        self.tabela()