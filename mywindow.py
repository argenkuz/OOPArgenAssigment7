from PyQt6.QtWidgets import QMainWindow
from calculator import Ui_MainWindow

class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.expression = ""

    def initUI(self):
        self.pushButton_0.clicked.connect(lambda: self.append_number('0'))
        self.pushButton_1.clicked.connect(lambda: self.append_number('1'))
        self.pushButton_2.clicked.connect(lambda: self.append_number('2'))
        self.pushButton_3.clicked.connect(lambda: self.append_number('3'))
        self.pushButton_4.clicked.connect(lambda: self.append_number('4'))
        self.pushButton_5.clicked.connect(lambda: self.append_number('5'))
        self.pushButton_6.clicked.connect(lambda: self.append_number('6'))
        self.pushButton_7.clicked.connect(lambda: self.append_number('7'))
        self.pushButton_8.clicked.connect(lambda: self.append_number('8'))
        self.pushButton_9.clicked.connect(lambda: self.append_number('9'))
        self.pushButton_dot.clicked.connect(lambda: self.append_number('.'))
        self.pushButton_plus.clicked.connect(lambda: self.append_operator('+'))
        self.pushButton_minus.clicked.connect(lambda: self.append_operator('-'))
        self.pushButton_multiple.clicked.connect(lambda: self.append_operator('*'))
        self.pushButton_division.clicked.connect(lambda: self.append_operator('/'))
        self.pushButton_equal.clicked.connect(self.calculate_result)
        self.pushButton_ac.clicked.connect(self.clear_display)
        self.pushButton_pm.clicked.connect(self.change_sign)
        self.pushButton_percentage.clicked.connect(self.delete_number)

    def append_number(self, number):
        expression = self.lineEdit.text()
        new_text = expression + number
        self.lineEdit.setText(new_text)

    def append_operator(self, operator):
        current_text = self.lineEdit.text()
        if current_text[-1] in ['+', '-', '*', '/']:
            self.lineEdit.setText(current_text[:-1] + operator)
        else:
            self.lineEdit.setText(current_text + operator)

    def calculate_result(self):
        try:
            expression = self.lineEdit.text()
            if '/0' in expression:
                self.lineEdit.setText("undefined")
            else:
                result = eval(expression)
                self.lineEdit.setText(str(result))
        except Exception:
            self.lineEdit.setText("undefined")

    def clear_display(self):
        self.lineEdit.clear()

    def change_sign(self):
        current_text = self.lineEdit.text()
        if current_text[0] == '-':
            self.lineEdit.setText(current_text[1:])
        else:
            self.lineEdit.setText('-' + current_text)

    def delete_number(self):
        current_text = self.lineEdit.text()
        new_text = current_text[:-1]
        self.lineEdit.setText(new_text)

    def get_expression(self):
        return self.expression
