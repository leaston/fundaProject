import os
import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QComboBox, QSpinBox, QPushButton, \
    QGridLayout, QHBoxLayout, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt


# Classe ClickableLabel
class ClickableLabel(QLabel):
    def __init__(self, icon_path, callback, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap(icon_path).scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.callback = callback

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.callback()


# Classe MegaMenu
class MegaMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Mega Menu Example')
        self.setGeometry(100, 100, 1200, 50)

        # Chemin relatif vers le répertoire icons
        icon_dir = os.path.join(os.path.dirname(__file__), 'icons')
        self.setWindowIcon(QIcon(os.path.join(icon_dir, 'app-icon.png')))
        self.setWindowTitle('Funda')

        self.create_tabs()

    def create_tabs(self):
        tabs = QTabWidget()
        self.setCentralWidget(tabs)

        # Create tabs
        home_tab = QWidget()
        insertion_tab = QWidget()
        design_tab = QWidget()
        page_layout_tab = QWidget()
        reference_tab = QWidget()
        revision_tab = QWidget()
        view_tab = QWidget()
        help_tab = QWidget()

        # Add tabs to the widget
        tabs.addTab(home_tab, 'Home')
        tabs.addTab(insertion_tab, 'Insertion')
        tabs.addTab(design_tab, 'Design')
        tabs.addTab(page_layout_tab, 'Page Layout')
        tabs.addTab(reference_tab, 'Reference')
        tabs.addTab(revision_tab, 'Revision')
        tabs.addTab(view_tab, 'View')
        tabs.addTab(help_tab, 'Help')

        # Set layout for 'Home' tab
        home_layout = QGridLayout()
        insertion_layout = QGridLayout()
        design_layout = QGridLayout()
        page_layout = QGridLayout()
        reference_layout = QGridLayout()
        revision_layout = QGridLayout()
        view_layout = QGridLayout()
        help_layout = QGridLayout()

        home_tab.setLayout(home_layout)
        insertion_tab.setLayout(insertion_layout)
        design_tab.setLayout(design_layout)
        page_layout_tab.setLayout(page_layout)
        reference_tab.setLayout(reference_layout)
        revision_tab.setLayout(revision_layout)
        view_tab.setLayout(view_layout)
        help_tab.setLayout(help_layout)

        # Create QFrames for each sub-layout in 'Home' tab
        text_frame = QFrame()
        text_frame.setFrameShape(QFrame.Box)  # Bordure de type Box
        text_frame.setLineWidth(1)  # Largeur de la bordure
        text_layout = QGridLayout(text_frame)

        align_frame = QFrame()
        align_frame.setFrameShape(QFrame.Box)
        align_frame.setLineWidth(1)
        align_layout = QGridLayout(align_frame)

        style_frame = QFrame()
        style_frame.setFrameShape(QFrame.Box)
        style_frame.setLineWidth(1)
        style_layout = QGridLayout(style_frame)

        # Add QFrames to the main layout
        home_layout.addWidget(text_frame, 0, 0)
        home_layout.addWidget(align_frame, 0, 1)
        home_layout.addWidget(style_frame, 0, 2)

        # Add clickable labels with icons
        icon_dir = os.path.join(os.path.dirname(__file__), 'icons')
        icons = [
            (os.path.join(icon_dir, 'align-left.png'), self.align_left),
            (os.path.join(icon_dir, 'align-center.png'), self.align_center),
            (os.path.join(icon_dir, 'align-right.png'), self.align_right),
            (os.path.join(icon_dir, 'justify.png'), self.justify_text),
            (os.path.join(icon_dir, 'bold.png'), self.set_bold),
            (os.path.join(icon_dir, 'italic.png'), self.set_italic),
            (os.path.join(icon_dir, 'underline.png'), self.set_underline),
            (os.path.join(icon_dir, 'strikethrough.png'), self.set_strikethrough),
            (os.path.join(icon_dir, 'index.png'), self.set_index),
            (os.path.join(icon_dir, 'superscript.png'), self.set_superscript)
        ]

        # Populate text_layout
        text_labels = [
            ("icons/bold.png", self.set_bold),
            ("icons/italic.png", self.set_italic),
            ("icons/underline.png", self.set_underline),
            ("icons/strikethrough.png", self.set_strikethrough),
            ("icons/index.png", self.set_index),
            ("icons/superscript.png", self.set_superscript)
        ]
        for i, (icon_path, callback) in enumerate(text_labels):
            label = ClickableLabel(icon_path, callback)
            text_layout.addWidget(label, 0, i)

        # Populate align_layout
        align_labels = [
            ("icons/align-left.png", self.align_left),
            ("icons/align-center.png", self.align_center),
            ("icons/align-right.png", self.align_right),
            ("icons/justify.png", self.justify_text)
        ]
        for i, (icon_path, callback) in enumerate(align_labels):
            label = ClickableLabel(icon_path, callback)
            align_layout.addWidget(label, 0, i)

        # Populate style_layout
        style_labels = [
            ("icons/color.png", self.apply_color),
            ("icons/highlight.png", self.apply_highlight)
        ]
        for i, (icon_path, callback) in enumerate(style_labels):
            label = ClickableLabel(icon_path, callback)
            style_layout.addWidget(label, 0, i)

    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignLeft)

    def align_center(self):
        self.textEdit.setAlignment(Qt.AlignCenter)

    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignRight)

    def justify_text(self):
        self.textEdit.setAlignment(Qt.AlignJustify)

    def set_bold(self):
        font = self.textEdit.font()
        font.setBold(not font.bold())
        self.textEdit.setFont(font)

    def set_italic(self):
        font = self.textEdit.font()
        font.setItalic(not font.italic())
        self.textEdit.setFont(font)

    def set_underline(self):
        font = self.textEdit.font()
        font.setUnderline(not font.underline())
        self.textEdit.setFont(font)

    def set_strikethrough(self):
        font = self.textEdit.font()
        font.setStrikethrough(not font.strikethrough())
        self.textEdit.setFont(font)

    def set_index(self):
        font = self.textEdit.font()
        font.setIndex(not font.index())
        self.textEdit.setFont(font)

    def set_superscript(self):
        font = self.textEdit.font()
        font.setSuperscript(not font.superscript())
        self.textEdit.setFont(font)

    def apply_color(self):
        pass  # Implement color application logic

    def apply_highlight(self):
        pass  # Implement highlight application logic


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MegaMenu()
    window.show()
    sys.exit(app.exec_())
