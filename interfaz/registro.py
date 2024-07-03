from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QLineEdit

class RegistroWindow():
    def __init__(self):
        self.v=uic.loadUi("interfaz/registro.ui")
        self.v.show()
        
    