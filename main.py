from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.list1 = ["камінь","ножиці","папір"]
        self.ui.pushButton.clicked.connect(self.button)
        self.ui.pushButton_2.clicked.connect(self.button2)
        self.ui.pushButton_3.clicked.connect(self.button3)

    def button(self):
        n = random.choice(self.list1)
        self.ui.pushButton_4.setText(n)
        if self.ui.pushButton_4.text() == "папір":
            self.ui.label.setText('Ти програв')
        elif self.ui.pushButton_4.text() == "ножиці":
            self.ui.label.setText('Ти виграв')
        elif self.ui.pushButton_4.text() == "камінь":
            self.ui.label.setText('Нічия')

    def button2(self):
        n = random.choice(self.list1)
        self.ui.pushButton_4.setText(n)
        if self.ui.pushButton_4.text() == "папір":
            self.ui.label.setText('Ти виграв')
        elif self.ui.pushButton_4.text() == "ножиці":
            self.ui.label.setText('Нічия')
        elif self.ui.pushButton_4.text() == "камінь":
            self.ui.label.setText('Ти програв')

    def button3(self):
        n = random.choice(self.list1)
        self.ui.pushButton_4.setText(n)
        if self.ui.pushButton_4.text() == "папір":
            self.ui.label.setText('Нічия')
        elif self.ui.pushButton_4.text() == "ножиці":
            self.ui.label.setText('Ти програв')
        elif self.ui.pushButton_4.text() == "камінь":
            self.ui.label.setText('Ти виграв')
    
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()