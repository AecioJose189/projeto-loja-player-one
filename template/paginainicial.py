# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paginainicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inicial(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(534, 409)
        self.botao_camisas = QtWidgets.QPushButton(Dialog)
        self.botao_camisas.setGeometry(QtCore.QRect(20, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.botao_camisas.setFont(font)
        self.botao_camisas.setObjectName("botao_camisas")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 0, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 60, 471, 261))
        self.label.setStyleSheet("image: url(:/produtos/logos/capa-pronta2.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.botao_shorts = QtWidgets.QPushButton(Dialog)
        self.botao_shorts.setGeometry(QtCore.QRect(20, 190, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.botao_shorts.setFont(font)
        self.botao_shorts.setObjectName("botao_shorts")
        self.botao_moletons = QtWidgets.QPushButton(Dialog)
        self.botao_moletons.setGeometry(QtCore.QRect(20, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.botao_moletons.setFont(font)
        self.botao_moletons.setObjectName("botao_moletons")
        self.botao_chapeus = QtWidgets.QPushButton(Dialog)
        self.botao_chapeus.setGeometry(QtCore.QRect(20, 240, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.botao_chapeus.setFont(font)
        self.botao_chapeus.setObjectName("botao_chapeus")
        self.botao_acessorios = QtWidgets.QPushButton(Dialog)
        self.botao_acessorios.setGeometry(QtCore.QRect(20, 290, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.botao_acessorios.setFont(font)
        self.botao_acessorios.setObjectName("botao_acessorios")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(140, 370, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(130, 330, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.botao_logout = QtWidgets.QPushButton(Dialog)
        self.botao_logout.setGeometry(QtCore.QRect(20, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.botao_logout.setFont(font)
        self.botao_logout.setObjectName("botao_logout")
        self.botao_carrinho = QtWidgets.QPushButton(Dialog)
        self.botao_carrinho.setGeometry(QtCore.QRect(40, 330, 41, 31))
        self.botao_carrinho.setStyleSheet("image: url(:/icons/icones/carr.png);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width: 2px;\n"
"border-color:black;")
        self.botao_carrinho.setText("")
        self.botao_carrinho.setObjectName("botao_carrinho")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 10, 71, 71))
        self.label_7.setStyleSheet("image: url(:/icons/icones/Gamepad(1).png);\n"
"image: url(:/icons/icones/Gamepad (3).png);")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.botao_camisas.setText(_translate("Dialog", "Camisas"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt;\">NOVA COLEÇÃO</span></p></body></html>"))
        self.botao_shorts.setText(_translate("Dialog", "Shorts"))
        self.botao_moletons.setText(_translate("Dialog", "Moletons"))
        self.botao_chapeus.setText(_translate("Dialog", "Chapéus"))
        self.botao_acessorios.setText(_translate("Dialog", "Acessórios"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">NA COMPRA DE R$130,00 EM PRODUTOS</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt;\">GANHE 20% DE DESCONTO</span></p></body></html>"))
        self.botao_logout.setText(_translate("Dialog", "log-out"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))

import template.imgicons
import template.produtos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Inicial()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
