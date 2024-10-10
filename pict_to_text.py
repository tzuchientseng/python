import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit
from PyQt5.QtGui import QPixmap, QClipboard
from PIL import Image
import pytesseract

# 設定 Tesseract 執行檔路徑 (替換為你的實際安裝路徑)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\GOOD-PC\AppData\Local\Programs\Tesseract-OCR'

class OCRApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image OCR Parser')

        layout = QVBoxLayout()

        self.label = QLabel('Select an image to parse text:')
        layout.addWidget(self.label)

        self.image_label = QLabel()
        layout.addWidget(self.image_label)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)  # 設定為只讀模式
        layout.addWidget(self.text_edit)

        select_button = QPushButton('Select Image', self)
        select_button.clicked.connect(self.open_image)
        layout.addWidget(select_button)

        copy_button = QPushButton('Copy Text', self)
        copy_button.clicked.connect(self.copy_text)
        layout.addWidget(copy_button)

        self.setLayout(layout)

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Image files (*.jpg *.png)')
        if file_name:
            # Display selected image
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap)

            # Use Tesseract OCR to parse text from the image
            img = Image.open(file_name)
            text = pytesseract.image_to_string(img)

            # Display the parsed text in QTextEdit
            self.text_edit.setPlainText(text)

    def copy_text(self):
        # Get the text from QTextEdit
        text = self.text_edit.toPlainText()

        # Copy text to clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

        # Optional: Show message to the user
        self.label.setText('Text copied to clipboard!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OCRApp()
    ex.show()
    sys.exit(app.exec_())
