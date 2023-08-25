from PyQt5.QtWidgets import QDialog
from template.paginainicial import Ui_Inicial
from template.shorts import Ui_Shorts

from modulos.shorts import paginashorts
from modulos.camisas import paginacamisas
from modulos.broches import paginabroches
from modulos.chapeus import paginachapeus
from modulos.moletons import paginamoletom
class paginainicial(QDialog):
    def __init__(self, tela_inicial, *args, **argvs):
        super(paginainicial, self).__init__(*args, **argvs)
        self.ui = Ui_Inicial()
        self.ui.setupUi(self)
        self.ui.botao_logout.clicked.connect(self.sair)
        self.ui.botao_shorts.clicked.connect(self.shorts)
        self.ui.botao_camisas.clicked.connect(self.camisas)
        self.ui.botao_acessorios.clicked.connect(self.broches)
        self.ui.botao_chapeus.clicked.connect(self.chapeus)
        self.ui.botao_moletons.clicked.connect(self.moletom)
        self.tela_inicial = tela_inicial
    def sair(self):
        self.window = self.tela_inicial.show()
        self.clearMask()
        self.destroy()
    def shorts(self):
        self.window = paginashorts(self)
        self.window.show()
        self.hide()
    def camisas(self):
        self.window = paginacamisas(self)
        self.window.show()
        self.hide()
    def broches(self):
        self.window = paginabroches(self)
        self.window.show()
        self.hide()
    def chapeus(self):
        self.window = paginachapeus(self)
        self.window.show()
        self.hide()
    def moletom(self):
        self.window = paginamoletom(self)
        self.window.show()
        self.hide()
