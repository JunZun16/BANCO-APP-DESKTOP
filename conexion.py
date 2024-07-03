import sqlite3

#SE CREA LA CONEXION
class Conexion():
    def __init__ (self):
        try:
            self.con=sqlite3.connect("banco.db")
            self.creartablas()
        except Exception as ex:
            print(ex)
#SE CRA LA TABLA
    def creartablas(self):
        sql_create_table1="""CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            usuario TEXT UNIQUE,
            clave TEXT)"""
        cur=self.con.cursor()
        cur.execute(sql_create_table1)
        cur.close()

#RETORNAR LA CONEXION
    def conectar(self):
            return self.con
            
           
