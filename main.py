import sys
from PyQt5.QtWidgets import QApplication
from programm_classes import KeysManager

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = KeysManager()
    main.show()
    sys.exit(app.exec_())
