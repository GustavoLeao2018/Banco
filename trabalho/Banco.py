#!/bin/env python3
"""Banco de dados de um estoque."""
from sqlite3 import *


class Banco:
    def conectar(self):
        return connect("banco.db")
    def fechar(self, db):
        db.close()

    def executar(self, sql, opcao, *args):
        db = self.conectar()
        cursor = db.cursor()
        if opcao == None:
            cursor.execute(sql)
        elif opcao == 'insert':
            cursor.execute(sql, *args)
            db.commit()
        elif opcao == 'select':
            itens = cursor.execute(sql)
            lista = []
            for item in itens.fetchall():
                lista.append(item)
            self.fechar(db)
            return lista
        elif opcao == 'select-quantidade':
            itens = cursor.execute(sql)
            lista = []
            for item in itens.fetchall():
                lista.append(item)
            self.fechar(db)
            return len(lista)
        elif opcao == 'delete':
            cursor.execute(sql, *args)
            db.commit()
        elif opcao == 'update':
            cursor.execute(sql, *args)
            db.commit()
        self.fechar(db)

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
        self.executar(sql, None)

    def inserir_produto(self, *args):
        sql = "INSERT INTO produto (produto, tipo, preco_unitario, quantidade) VALUES (?, ?, ?, ?);"
        self.executar(sql, 'insert', *args)

    def ler_produtos(self):
        sql = "SELECT * FROM produto;"
        return self.executar(sql, 'select')

    def apagar_produto(self, *args):
        sql = "DELETE FROM produto WHERE id = ?;"
        self.executar(sql, 'delete', *args)

    def ler_quantidade(self):
        sql = "SELECT * FROM produto;"
        return self.executar(sql, 'select-quantidade')

    def editar_produto(self, *args):
        sql = "UPDATE produto SET quantidade = ? WHERE id = ?"
        self.executar(sql, 'update', *args)


    def __init__(self):
        self.tabela()