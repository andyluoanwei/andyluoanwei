import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QVBoxLayout

class Application(QWidget):
    def __init__(self):
        super().__init__()

    
    def initUI(self):
        okButton = QPushButton("OK")    
        cancelButton = QPushButton("Cancel")

        