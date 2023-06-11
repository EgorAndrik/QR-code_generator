import sys
import segno
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR generator")
        self.setFixedSize(QSize(450, 550))
        self.layout = QVBoxLayout()
        self.container = QWidget()

        pixmap = QPixmap("QR_start.png")
        self.imgQR = QLabel()
        self.imgQR.setPixmap(pixmap)

        self.input = QLineEdit()
        self.input.setFixedSize(400, 50)

        self.button = QPushButton("Create")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.crearQR)
        self.button.setFixedSize(100, 50)

        self.conectWidgets()

    def conectWidgets(self):
        self.layout.addWidget(self.imgQR, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def crearQR(self):
        qrcode = segno.make_qr(self.input.text())
        qrcode.save("QR_code.png", dark="#09e3eb", border=2, scale=10)
        pixmap = QPixmap("QR_code.png")
        self.imgQR.setPixmap(pixmap)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
