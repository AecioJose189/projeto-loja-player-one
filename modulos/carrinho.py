from dataclasses import dataclass
from PyQt5.QtWidgets import QDialog
from modulos.carrinho_funcs import get_carrinho
from template.carrinho import Ui_Carrinho
from PyQt5 import QtCore, QtWidgets


@dataclass
class Item:
    image: str
    quantity: int
    price: float


class PaginaCarrinho(QDialog):
    def __init__(self, tela_inicial, *args, **argvs):
        super(PaginaCarrinho, self).__init__(*args, **argvs)
        self.ui = Ui_Carrinho()
        self.ui.setupUi(self)
        self.tela_inicial = tela_inicial
        self.carrinho = [
            Item(item['imagem'], item['quantidade'], item['preco']) for item in get_carrinho()
        ]

        for item in self.carrinho:
            self.addItem(item)

    def voltando(self):
        self.window = self.tela_inicial.show()
        self.clearMask()
        self.destroy()

    def addItem(self, item: Item):
        item_layout_widget = QtWidgets.QWidget()

        item_layout_widget.setFixedSize(QtCore.QSize(678, 80))

        item_layout = QtWidgets.QHBoxLayout(item_layout_widget)
        item_layout.setContentsMargins(0, 0, 0, 0)

        item_image = QtWidgets.QLabel(item_layout_widget)
        item_image.setText("")
        item_image.setStyleSheet(
            f"image: url({item.image});")

        item_price = QtWidgets.QLabel(item_layout_widget)
        preco_str = f'{item.price * item.quantity:.2f}'.replace('.', ',')
        item_price.setText(f"R$ {preco_str}")
        item_price.setStyleSheet("font: 75 12pt \"Arial\";")
        item_price.setAlignment(QtCore.Qt.AlignCenter)

        item_quantity = QtWidgets.QSpinBox(item_layout_widget)
        item_quantity.setMinimum(1)
        item_quantity.setValue(item.quantity)
        item_quantity.valueChanged.connect(lambda value: item_price.setText(
            self.get_string_reais(item.price * value)))

        item_layout.addWidget(item_image)
        item_layout.addWidget(item_quantity)
        item_layout.addWidget(item_price)

        self.ui.vBox.addWidget(item_layout_widget)

    def get_string_reais(self, value: float):
        return f'R$ {value:.2f}'.replace('.', ',')
