from PyQt6 import uic
from PyQt6.QtCore import QDate

from PyQt6.QtWidgets import QMessageBox,QTableWidgetItem


from data.deposito import DepositoData
from data.estados import EstadosData
from data.historial import HistorialData
from data.transferencia import TransferenciaData
from model.movimientos import Transferencia
from model.movimientos import DepositoInternacional



class MainWindow1():
    def __init__(self):
        self.main=uic.loadUi("interfaz/main.ui")
        self.initGUI()
        self.main.showMaximized()
        
    def initGUI(self):
        self.main.btn_Registrar_Transferencia.triggered.connect(self.AbrirRegistro)
        self.main.btn_Reportar_Transferencia.triggered.connect(self.AbrirDeposito)
        self.main.btn_Historial_de_Transferencias.triggered.connect(self.AbrirHistorial)
        
        self.registro=uic.loadUi("interfaz/registro.ui")
        self.deposito=uic.loadUi("interfaz/deposito.ui")
        self.historial=uic.loadUi("interfaz/historial.ui")
       
        
    def AbrirRegistro(self):
        self.registro.btnRegistrar.clicked.connect(self.registrarTransaccion)
        self.registro.show()
        
    def AbrirDeposito(self):
        self.deposito.btnRegistrar.clicked.connect(self.RegistrarDeposito)
        self.deposito.show()
        self.llenarComboCiudades()
        
    def AbrirHistorial(self):
        self.historial.btnBuscar.clicked.connect(self.buscar)
        self.historial.show()
        self.historial.tblHistorial.setColumnWidth(0,30)
        self.historial.tblHistorial.setColumnWidth(1,200)
        self.historial.tblHistorial.setColumnWidth(3,150)
        self.historial.tblHistorial.setColumnWidth(4,220)
        self.historial.tblHistorial.setColumnWidth(5,100)
        
    
        #self.llenarTablaHistorial()
        
    ####### LA VENTANA DE REGISTRO DE TRASNFERENCIAS###########
    def registrarTransaccion(self):
        if self.registro.cbTipo.currentText() == "----Seleccione una opcion":
            mBox=QMessageBox()
            mBox.setText("Debes Seleccionar el tipo de documento")
            mBox.exec()
            self.registro.cbTipo.setFocus()
            
        elif len(self.registro.txtDocumento.text())<3:
            mBox=QMessageBox()
            mBox.setText("Ingresa un Numero de Documento Valido")
            mBox.exec()
            self.registro.txtDocumento.setFocus()
            
        elif self.registro.cbMotivo.currentText() == "----Seleccione una opcion":
            mBox=QMessageBox()
            mBox.setText("Debes Seleccionar el Motivo")
            mBox.exec()
            self.registro.cbMotivo.setFocus()
            
        elif not self.registro.txtMonto.text().isnumeric() or self.registro.txtMonto.text()=="0":
            mBox=QMessageBox()
            mBox.setText("Ingresa un Monto Valido")
            mBox.exec()
            self.registro.txtMonto.setText("0")
            self.registro.txtMonto.setFocus()
        
        else:
            transferencia=Transferencia(
                tipo=self.registro.cbTipo.currentText(),
                documento=self.registro.txtDocumento.text(),
                motivo=self.registro.cbMotivo.currentText(),
                monto=float(self.registro.txtMonto.text()),
                dolares=self.registro.checkDolares.isChecked(),
                internacional=self.registro.checkInternacional.isChecked())
            
            objData=TransferenciaData()
            mBox=QMessageBox()
            if objData.registrar(info=transferencia):
                mBox.setText("Registro de Transferencia Existoso")
                self.limpiarcampostransferencias()
            else:
                mBox.setText("Registro de Transferencia Fallido")
                
            mBox.exec()
               
    def limpiarcampostransferencias(self):
        self.registro.cbTipo.setCurrentIndex(0)
        self.registro.txtDocumento.setText("")
        self.registro.cbMotivo.setCurrentIndex(0)
        self.registro.txtMonto.setText("0")
        self.registro.checkDolares.setChecked(False)
        self.registro.checkInternacional.setChecked(False)
        self.registro.cbTipo.setFocus()
    
    ####### LA VENTANA DE DEPOSITOS ###########
    def llenarComboCiudades(self):
        objData=EstadosData()
        datos=objData.listaEstados()
        
        for item in datos:
            self.deposito.cbLugar.addItem(item[1])

    def validarCamposObligatorios(self)->bool:
        if not self.deposito.txtDocumento.text() or not self.deposito.txtPrimerApellido.text() or not self.deposito.txtPrimerNombre.text() or not self.deposito.txtMonto.text():
            mBox=QMessageBox()
            mBox.setText("Debe de llenar los campos obligatorios")
            mBox.exec()
            return False
        
        elif not self.deposito.txtMonto.text().isnumeric() or float(self.deposito.txtMonto.text())<=0:
            mBox=QMessageBox()
            mBox.setText("""Debe de llenar los campos obligatorios
                        El monto debe ser mayor a cero """)
            mBox.exec()
            self.deposito.txtMonto.setText("0")
            self.deposito.txtMonto.setFocus()
            return False
            
        elif self.deposito.cbMotivo.currentText() == "----Seleccione una opcion":
            mBox=QMessageBox()
            mBox.setText("Debe de llenar los campos obligatorios")
            mBox.exec()
            self.deposito.cbMotivo.setFocus()
            return False
        
        elif self.deposito.cbTipo.currentText() == "----Seleccione una opcion":
            mBox=QMessageBox()
            mBox.setText("Debe de llenar los campos obligatorios")
            mBox.exec()
            self.deposito.cbTipo.setFocus()
            return False
        
        elif not self.deposito.checkTerminos.isChecked():
            mBox=QMessageBox()
            mBox.setText("Debe de llenar los campos obligatorios")
            mBox.exec()
            self.deposito.checkTerminos.setFocus()
            return False
        else:
            return True
    
    def RegistrarDeposito(self):
        
        if not self.validarCamposObligatorios():
            mBox=QMessageBox()
            mBox.setText("Debe de llenar los campos obligatorios")
            mBox.exec()
        else:
            fechaN=self.deposito.txtFecha.date().toPyDate()
            
            deposito=DepositoInternacional(
                tipo=self.deposito.cbTipo.currentText(),
                documento=self.deposito.txtDocumento.text(),
                motivo=self.deposito.cbMotivo.currentText(),
                internacional=True,
                dolares=True,
                monto=float(self.deposito.txtMonto.text()),
                nombre1=self.deposito.txtPrimerNombre.text(),
                nombre2=self.deposito.txtSegundoNombre.text(),
                apellido1=self.deposito.txtPrimerApellido.text(),
                apellido2=self.deposito.txtSegundoApellido.text(),
                sexo=self.deposito.cbSexo.currentText(),
                fechaNacimiento=fechaN,
                lugarNacimiento=self.deposito.cbLugar.currentText(),
                terminos=self.deposito.checkTerminos.isChecked()
                )
            
            objData=DepositoData()
            mBox=QMessageBox()
            if objData.registrar(info=deposito):
                mBox.setText("Deposito Registrado")
                self.limpiarcamposdeposito()
            else:
                mBox.setText("Deposito NO Registrado")
                
            mBox.exec()
        
    def limpiarcamposdeposito(self):
            
        self.deposito.cbTipo.setCurrentIndex(0)
        self.deposito.txtDocumento.setText("")
        self.deposito.cbMotivo.setCurrentIndex(0)
        self.deposito.txtMonto.setText("0")
        self.deposito.cbTipo.setFocus()
        self.deposito.txtPrimerNombre.setText("")
        self.deposito.txtSegundoNombre.setText("")
        self.deposito.txtPrimerApellido.setText("")
        self.deposito.txtSegundoApellido.setText("")
        self.deposito.cbSexo.setCurrentIndex(0)
        self.deposito.cbLugar.setCurrentIndex(0)
        self.deposito.checkTerminos.isChecked()
        mifecha=QDate(2000,1,1)
        self.deposito.txtFecha.setDate(mifecha)    
        
        
    #####lA VENTANA DE HISTORIAL DE TRANSFERENCIAS#######
    
    def buscar(self):
        his=HistorialData()
        data=his.buscarPorFecha(self.historial.txtDesde.date().toPyDate(),self.historial.txtHasta.date().toPyDate(),self.historial.cbTipo.currentText(),self.historial.txtDocumento.text())
        fila=0
        nombre= None
        self.historial.tblHistorial.setRowCount(len(data))
        for item in data:
            self.historial.tblHistorial.setItem(fila,0,QTableWidgetItem(str(item[0])))
            
            if nombre:
                self.historial.tblHistorial.setItem(fila,1,QTableWidgetItem(nombre))
            else:
                self.historial.tblHistorial.setItem(fila,1,QTableWidgetItem("{} {} {} {}".format(str(item[9]),str(item[10]),str(item[11]),str(item[12]))))
                nombre="{} {} {} {}".format(str(item[9]),str(item[10]),str(item[11]),str(item[12]))
            if item[6]=="True":
                self.historial.tblHistorial.setItem(fila,2,QTableWidgetItem("USD  " + str(item[2])))
            else:
                self.historial.tblHistorial.setItem(fila,2,QTableWidgetItem("MXN  " + str(item[2])))
                
            if item[5]=="True":
                self.historial.tblHistorial.setItem(fila,4,QTableWidgetItem("Internacional/"+ str(item[8])))
            else:
                self.historial.tblHistorial.setItem(fila,4,QTableWidgetItem("Nacional/     "+ str(item[8]) ))
            
            self.historial.tblHistorial.setItem(fila,3,QTableWidgetItem(str(item[7])))
            
            if item[17]=="True":
                self.historial.tblHistorial.setItem(fila,5,QTableWidgetItem(" SI "))
            else:
                self.historial.tblHistorial.setItem(fila,5,QTableWidgetItem(" NO " ))
            
                                                
            fila=fila+1
            
    def llenarTablaHistorial(self):
        pass
    