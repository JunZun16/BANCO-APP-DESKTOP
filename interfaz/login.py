from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QLineEdit

from data.usuario import UsuarioData
from interfaz.main import MainWindow1
from model.usuario import Usuario

class Login():
    
    def __init__(self):
        self.login=uic.loadUi("interfaz/login.ui")
        self.initGUI()
        self.login.lblMensaje.setText("")
        self.login.show()
        
    def ingresar(self):
        if len(self.login.txtUsuario.text())<3:
            self.login.lblMensaje.setText("Ingrese Usuario Valido")
            self.login.txtUsuario.setFocus()
        
        elif len(self.login.txtClave.text())<3:
            self.login.lblMensaje.setText("Ingrese Contraseña Valida")
            self.login.txtClave.setFocus()
        
        else:
            self.login.lblMensaje.setText("")
            usu=Usuario(usuario=self.login.txtUsuario.text(),clave=self.login.txtClave.text())
            usuData=UsuarioData()
            res=usuData.login(usu)
            if res:
                
                self.main=MainWindow1()
                self.login.hide()
                
            else:
                self.login.lblMensaje.setText("Datos de acceso incorrecto")
    
    def initGUI(self):
           self.login.btnAcceder.clicked.connect(self.ingresar)