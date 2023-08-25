# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cadastro(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 300)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 10, 151, 121))
        self.label_3.setStyleSheet("image: url(:/icons/icones/Gamepad.png);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.input_usuario = QtWidgets.QLineEdit(Dialog)
        self.input_usuario.setGeometry(QtCore.QRect(90, 150, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        self.input_usuario.setFont(font)
        self.input_usuario.setObjectName("input_usuario")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.input_senha = QtWidgets.QLineEdit(Dialog)
        self.input_senha.setGeometry(QtCore.QRect(90, 180, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        self.input_senha.setFont(font)
        self.input_senha.setStyleSheet("")
        self.input_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_senha.setObjectName("input_senha")
        self.botao_cadastrar = QtWidgets.QPushButton(Dialog)
        self.botao_cadastrar.setGeometry(QtCore.QRect(110, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.botao_cadastrar.setFont(font)
        self.botao_cadastrar.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:black;\n"
"}\n"
"QPushButton:pressed{\n"
"color:black;\n"
"background-color:white;\n"
"border-style:outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:black;\n"
"}")
        self.botao_cadastrar.setObjectName("botao_cadastrar")
        self.botao_voltar = QtWidgets.QPushButton(Dialog)
        self.botao_voltar.setGeometry(QtCore.QRect(10, 260, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.botao_voltar.setFont(font)
        self.botao_voltar.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:black;\n"
"}\n"
"QPushButton:pressed{\n"
"color:black;\n"
"background-color:white;\n"
"border-style:outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:black;\n"
"}")
        self.botao_voltar.setObjectName("botao_voltar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tela de cadastro"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "Usuário"))
        self.input_usuario.setPlaceholderText(_translate("Dialog", "Digite seu usuário"))
        self.label_5.setText(_translate("Dialog", "Senha"))
        self.input_senha.setPlaceholderText(_translate("Dialog", "Digite sua senha"))
        self.botao_cadastrar.setText(_translate("Dialog", "Cadastrar"))
        self.botao_voltar.setText(_translate("Dialog", "Voltar"))
        
import template.imgicons
import template.produtos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Cadastro()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
