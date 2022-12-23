from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUi

import sys
import random

class Form(QMainWindow):

    def __init__(self):
            super(Form, self).__init__()

            loadUi('random.ui', self)

            self.output.clicked.connect(self.output_game)


    def output_game(self):
        try:
            randomer = random.randint(1, 10)
            user_num = int(self.input.text())
            print(randomer)
            if user_num <=10:
                if user_num ==randomer:
                    self.answer.setText("Вы угадали !")
                    self.answer2.setText(f"Мое число: {randomer}")


                else:
                    self.answer.setText("Вы не угадали !")
                    self.answer2.setText(f"Мое число: {randomer}")
            else:
                self.answer.setText("Введите число от 1 до 10")
        except ValueError:
                self.answer.setText("Введите число !!!")


            

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

