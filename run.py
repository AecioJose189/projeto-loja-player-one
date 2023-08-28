import sys
from PyQt5.QtWidgets import QDialog, QApplication
from modulos.login import Login


def main():
    app = QApplication(sys.argv)
    if QDialog.Accepted:
        window = Login()
        window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
