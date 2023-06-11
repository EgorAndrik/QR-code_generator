import sys
import segno
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtGui import QPixmap, QFont


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

        self.firstTitle = QLabel("Enter link:")
        self.firstTitle.setFont(QFont('Arial', 20))
        self.firstTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.firstTitle.setFixedSize(400, 50)

        self.input = QLineEdit()
        fontInput = self.input.font()
        fontInput.setPointSize(14)
        self.input.setFont(fontInput)
        self.input.setFixedSize(400, 50)

        self.button = QPushButton("Create")
        self.button.setStyleSheet("text-align:center; font-size: 20px")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.crearQR)
        self.button.setFixedSize(100, 50)

        self.conectWidgets()

    def conectWidgets(self):
        self.layout.addWidget(self.imgQR, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.firstTitle, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def crearQR(self):
        qrcode = segno.make_qr(self.input.text())
        qrcode.save("QR_code.png", dark="#0771ab", border=2, scale=10)
        pixmap = QPixmap("QR_code.png")
        self.imgQR.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
