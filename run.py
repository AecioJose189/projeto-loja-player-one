import sys
from PyQt5.QtWidgets import QDialog, QApplication
from modulos.login import Login

def main() -> None:
    app = QApplication(sys.argv)
    print("Iniciando...")

    if QDialog.Accepted:
        print("Login")
        window = Login()
        window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

