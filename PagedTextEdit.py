from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from CustomTextEdit import CustomTextEdit


class PagedTextEdit(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.textEdit = CustomTextEdit()
        self.layout.addWidget(self.textEdit)

        self.prev_button = QPushButton("Previous")
        self.page_label = QLabel("1/1")
        self.next_button = QPushButton("Next")

        self.layout.addWidget(self.prev_button)
        self.layout.addWidget(self.page_label)
        self.layout.addWidget(self.next_button)

        self.pages = []
        self.current_page = 0
        self.update_pages()

    def update_pages(self):
        text = self.textEdit.toPlainText()
        self.pages = text.split('\n\n')  # Split text into pages based on double newlines
        self.show_page(0)

    def show_page(self, index):
        if 0 <= index < len(self.pages):
            self.current_page = index
            self.textEdit.setPlainText(self.pages[index])
            self.page_label.setText(f'Page {self.current_page + 1} / {len(self.pages)}')
