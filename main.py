#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtGui import QIcon
from calculator import Ui_Dialog

class Calculator(QDialog):
    def __init__(self):
        super().__init__()
        self.just_calculated = False
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("tapcalc.png"))
        self.ui.btn0.clicked.connect(self.button_clicked)
        self.ui.btn1.clicked.connect(self.button_clicked)
        self.ui.btn2.clicked.connect(self.button_clicked)
        self.ui.btn3.clicked.connect(self.button_clicked)
        self.ui.btn4.clicked.connect(self.button_clicked)
        self.ui.btn5.clicked.connect(self.button_clicked)
        self.ui.btn6.clicked.connect(self.button_clicked)
        self.ui.btn7.clicked.connect(self.button_clicked)
        self.ui.btn8.clicked.connect(self.button_clicked)
        self.ui.btn9.clicked.connect(self.button_clicked)
        self.ui.addition.clicked.connect(self.button_clicked)
        self.ui.division.clicked.connect(self.button_clicked)
        self.ui.multiplication.clicked.connect(self.button_clicked)
        self.ui.substraction.clicked.connect(self.button_clicked)
        self.ui.decimal.clicked.connect(self.button_clicked)
        self.ui.equal.clicked.connect(self.answer)
        self.ui.AC.clicked.connect(self.clear)
        self.ui.C.clicked.connect(self.delete)

        
    def button_clicked(self):
        button = self.sender()

        text = button.text()

        current_text = self.ui.lineEdit.text()
        operators = "+-*/."
        if current_text == "" and text in operators:
            return
        if self.just_calculated:
            current_text = ""
            self.ui.lineEdit.clear()
            self.just_calculated = False
        if len(current_text) > 0:
            last = current_text[-1]

            if last in "+-*/." and text in "+-*/.":
                return

        self.ui.lineEdit.setText(current_text + text)
        

    def answer(self):
        try:
            expression = self.ui.lineEdit.text()

            answer = round(eval(expression), 6)

            if answer == int(answer):
                self.ui.lineEdit.setText(str(int(answer)))
            else:
                self.ui.lineEdit.setText(str(answer))

            self.just_calculated = True

        except:
            self.ui.lineEdit.setText("Error")


    def clear(self):
        self.ui.lineEdit.setText("")

    def delete(self):
        current = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(current[:-1])




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())