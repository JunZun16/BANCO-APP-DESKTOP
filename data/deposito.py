import conexion as con 
from model.movimientos import DepositoInternacional
from datetime import datetime

class DepositoData():
    def __init__(self):
        try:
            self.db=con.Conexion().conectar()
            self.cursor=self.db.cursor()
            sql_create_depositos="""CREATE TABLE IF NOT EXISTS depositos(
                                                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                        monto NUMERIC,
                                                                        tipo TEXT,
                                                                        documento TEXT,
                                                                        internacional BOOLEAN,
                                                                        dolares BOOLEAN,
                                                                        fecha_registro DATETIME,
                                                                        motivo TEXT,
                                                                        pnombre TEXT,
                                                                        snombre TEXT,
                                                                        papellido TEXT,
                                                                        sapellido TEXT,
                                                                        sexo TEXT,
                                                                        fecha_nacimiento DATETIME,
                                                                        lugar_nacimiento TEXT,
                                                                        terminos BOOLEAN
                                                                        )"""
            self.cursor.execute(sql_create_depositos)
            self.db.commit()
            self.cursor.close()
            self.db.close()
            
        except Exception as ex:
            print(ex)
            
    def registrar(self,info:DepositoInternacional):
        fecha=datetime.now().strftime("%Y-%m-%d %H:%M")
        self.db=con.Conexion().conectar()
        self.cursor=self.db.cursor()
        self.cursor.execute("""
        INSERT INTO depositos 
        values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._monto,info._tipo,info._documento,info._internacional,info._dolares,fecha,info._motivo,info._nombre1,info._nombre2,info._apellido1,info._apellido2,info._sexo,info._fechaNacimiento,info._lugarNacimiento,info._terminos))
        self.db.commit()
        if self.cursor.rowcount==1:
           return True
        else:
            return False