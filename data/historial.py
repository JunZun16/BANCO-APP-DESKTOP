import conexion as con

class HistorialData():
    def buscarPorFecha(self,fechaDesde,fechaHasta,tipo,documento):
        
        self.db=con.Conexion().conectar()
        self.cursor=self.db.cursor()
        
        sql="""
        SELECT T.id as Transaccion,D.*,T.verificado FROM transferencias T
        INNER JOIN depositos D ON D.tipo=T.tipo and D.documento=T.documento
        WHERE T.fecha >='{}' and T.fecha <='{}' and D.documento='{}' and D.tipo='{}'
        and T.motivo=D.motivo and T.monto=D.monto
        """.format(fechaDesde,fechaHasta,documento,tipo)
        
        res=self.cursor.execute(sql)
        datos=res.fetchall()
        return datos