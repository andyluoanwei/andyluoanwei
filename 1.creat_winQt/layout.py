import sys
from PyQt5.QtWidgets import QWidget,  QLabel, QApplication

class Layout(QWidget):
    def __init__(self):
        super().__init__()
        self.initLayoutUI()

    def initLayoutUI(self):
        label_1 = QLabel("Zet_code", self)
        label_1.move(15, 10)

        label_2 = QLabel("Tutorials", self)
        label_2.move(35, 40)

        label_3 = QLabel("For Programming", self)
        label_3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Layout()
    sys.exit(app.exec_())

