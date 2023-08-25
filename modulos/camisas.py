from PyQt5.QtWidgets import QDialog
from template.paginainicial import Ui_Inicial
from template.camisas import Ui_Camisas

class paginacamisas(QDialog):
    def __init__(self, tela_inicial, *args, **argvs):
        super(paginacamisas, self).__init__(*args, **argvs)
        self.ui = Ui_Camisas()
        self.ui.setupUi(self)
        self.ui.botao_voltar.clicked.connect(self.voltando)
        self.tela_inicial = tela_inicial
    def voltando(self):
        self.window = self.tela_inicial.show()
        self.clearMask()
        self.destroy()
