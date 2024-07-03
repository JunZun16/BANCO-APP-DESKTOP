from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

from interfaz.login import Login

class Banco():
    def __init__(self):
        self.app=QApplication([])
        self.login=Login()
        self.app.exec()
        
