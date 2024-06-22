import os

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QToolBar, QComboBox, QSpinBox, QSlider, QHBoxLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from CustomTextEdit import CustomTextEdit
from PagedTextEdit import PagedTextEdit
from actions import TextEditorActions
from menubar import create_menu


class MainWindow(QMainWindow):
    def __init__(self, new_instance_callback=None):
        super().__init__()

        self.setWindowTitle('Funda')
        self.setGeometry(100, 100, 1200, 800)

        # Chemin relatif vers le répertoire icons
        icon_dir = os.path.join(os.path.dirname(__file__), 'icons')
        self.setWindowIcon(QIcon(os.path.join(icon_dir, 'app-icon.png')))
        self.setWindowTitle('Funda')
        #---------------------------------------------------------------------

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Appliquer une couleur de fond pour les zones extérieures
        central_widget.setStyleSheet("background-color: #f0f0f0;")

        # Layout pour les boutons de contrôle (sous la barre d'outils)
        control_widget = QWidget()
        control_layout = QHBoxLayout(control_widget)

        # Slider pour zoom
        self.zoom_slider = QSlider(Qt.Horizontal)
        self.zoom_slider.setMinimum(-10)  # Minimum zoom level
        self.zoom_slider.setMaximum(10)  # Maximum zoom level
        self.zoom_slider.setValue(0)  # Start at the middle point
        self.zoom_slider.setTickPosition(QSlider.TicksBelow)
        self.zoom_slider.setTickInterval(1)
        self.zoom_slider.valueChanged.connect(self.handle_zoom)
        control_layout.addWidget(self.zoom_slider)

        # Widgets pour personnaliser la police et la taille de police
        self.font_combo = QComboBox()
        self.font_combo.addItems(["Arial", "Times New Roman", "Verdana"])
        self.font_combo.currentIndexChanged.connect(self.update_labels_font)
        control_layout.addWidget(self.font_combo)

        self.size_spinbox = QSpinBox()
        self.size_spinbox.setValue(12)
        self.size_spinbox.valueChanged.connect(self.update_labels_size)
        control_layout.addWidget(self.size_spinbox)

        # Ajouter les boutons de navigation de page de PagedTextEdit
        self.pagedTextEdit = PagedTextEdit()
        control_layout.addWidget(self.pagedTextEdit.prev_button)
        control_layout.addWidget(self.pagedTextEdit.page_label)
        control_layout.addWidget(self.pagedTextEdit.next_button)

        # Ajouter le widget de contrôle au layout principal
        main_layout.addWidget(control_widget)

        # Layout pour centrer la zone de saisie verticalement
        vertical_center_layout = QVBoxLayout()
        main_layout.addLayout(vertical_center_layout)
        vertical_center_layout.addStretch(1)

        # Layout pour centrer la zone de saisie horizontalement
        center_layout = QHBoxLayout()
        vertical_center_layout.addLayout(center_layout)
        vertical_center_layout.addStretch(1)

        self.textEdit = CustomTextEdit()
        center_layout.addStretch(1)
        center_layout.addWidget(self.textEdit)
        center_layout.addStretch(1)

        # Initialiser les actions avant de créer la barre d'outils
        self.actions = TextEditorActions(self, new_instance_callback)

        # Ajouter la barre d'outils et le menu
        self.create_toolbar()
        create_menu(self)

    def create_toolbar(self):
        self.toolbar = QToolBar("Main Toolbar")
        # self.toolbar.setStyleSheet("height: 100px;")  # Fixer la hauteur de la barre d'outils
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        # Ajouter des actions à la barre d'outils
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

    def update_labels_font(self, index):
        font = QFont()
        font.setFamily(self.font_combo.currentText())
        font.setPointSize(self.textEdit.font().pointSize())
        self.textEdit.setFont(font)

    def update_labels_size(self, size):
        font = QFont()
        font.setFamily(self.textEdit.font().family())
        font.setPointSize(size)
        self.textEdit.setFont(font)

    def handle_zoom(self, value):
        font = self.textEdit.font()
        base_size = 12
        font.setPointSize(base_size + value)
        self.textEdit.setFont(font)

        # Ajuster la largeur de la zone de saisie en fonction du zoom
        a4_base_width = int(210 * 3.78)  # Largeur A4 en pixels
        new_width = a4_base_width + value * 20  # Ajuster ce facteur selon vos besoins
        self.textEdit.setFixedWidth(new_width)
