import sys
import segno
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QComboBox
from PyQt6.QtGui import QPixmap, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR generator")
        self.setFixedSize(QSize(550, 700))
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
        self.input.setFixedSize(500, 50)

        self.secondTitel = QLabel("QR-code size:")
        self.secondTitel.setFont(QFont('Arial', 14))
        self.secondTitel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.secondTitel.setFixedSize(400, 50)

        self.combo = QComboBox(self)
        for i in range(4, 11, 2):
            self.combo.addItem(str(i))
        self.combo.setStyleSheet("text-align:center; font-size: 14px")
        self.combo.setFixedSize(100, 50)

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
        self.layout.addWidget(self.secondTitel, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.combo, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def crearQR(self):
        sizeQR = int(self.combo.currentText())
        qrcode = segno.make_qr(self.input.text())
        qrcode.save("QR_code.png", dark="#0771ab", border=2, scale=sizeQR)
        pixmap = QPixmap("QR_code.png")
        self.imgQR.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
