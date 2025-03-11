import sys
from PyQt6.QtWidgets import QApplication
from mywindow import Calculator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())