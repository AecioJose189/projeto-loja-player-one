from PyQt5.QtWidgets import QDialog
from template.paginainicial import Ui_Inicial
from template.shorts import Ui_Shorts

class paginashorts(QDialog):
    def __init__(self, tela_inicial, *args, **argvs):
        super(paginashorts, self).__init__(*args, **argvs)
        self.ui = Ui_Shorts()
        self.ui.setupUi(self)
        self.ui.botao_voltar.clicked.connect(self.voltando)
        self.tela_inicial = tela_inicial
    def voltando(self):
        self.window = self.tela_inicial.show()
        self.clearMask()
        self.destroy()