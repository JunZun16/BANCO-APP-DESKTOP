import conexion as con

class EstadosData():
    def listaEstados(self):
        self.db=con.Conexion().conectar()
        self.cursor=self.db.cursor()
        res=self.cursor.execute("""
                                SELECT * FROM ciudades order by nombre
                                """)
        estados=res.fetchall()
        return estados