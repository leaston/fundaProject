from PyQt5.QtWidgets import QMainWindow, QTextEdit, QToolBar, QVBoxLayout, QWidget, QSpinBox, QComboBox
from PyQt5.QtGui import QIcon
import os
from MegaMenuTabs import MegaMenu
from menubar import create_menu
from actions import TextEditorActions
from CustomTextEdit import CustomTextEdit


class TextEditor(QMainWindow):
    def __init__(self, new_instance_callback=None):
        super().__init__()

        self.new_instance_callback = new_instance_callback

        # Utilisation de CustomTextEdit au lieu de QTestEdit
        self.textEdit = CustomTextEdit()
        self.setCentralWidget(self.textEdit)

        # Chemin relatif vers le répertoire icons
        icon_dir = os.path.join(os.path.dirname(__file__), 'icons')
        self.setWindowIcon(QIcon(os.path.join(icon_dir, 'app-icon.png')))
        self.setWindowTitle('Funda')

        self.actions = TextEditorActions(self)
        self.menubar = create_menu(self)
# -------------------------------------------------------------------------
        '''central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Ajouter CustomTextEdit
        self.text_edit = CustomTextEdit()
        layout.addWidget(self.text_edit)'''
# -------------------------------------------------------------------------
        # Barre d'outils
        self.toolbar = QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)

        # Ajouter une barre d'outils
        self.toolbar = QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)
        self.toolbar.addAction(self.actions.newAction)
        self.toolbar.addAction(self.actions.openAction)
        self.toolbar.addAction(self.actions.saveAction)
        self.toolbar.addAction(self.actions.printAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actions.cutAction)
        self.toolbar.addAction(self.actions.copyAction)
        self.toolbar.addAction(self.actions.pasteAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actions.undoAction)
        self.toolbar.addAction(self.actions.redoAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actions.aboutAction)

        self.setGeometry(300, 300, 800, 600)

    def create_new_instance(self):
        if self.new_instance_callback:
            self.new_instance_callback()


