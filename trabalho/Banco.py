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
        self.fechar(self.db)

    def __init__(self):
        self.tabela()