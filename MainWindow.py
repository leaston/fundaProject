import os
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QToolBar, QComboBox, QSpinBox, QSlider, QHBoxLayout, \
    QLabel, QTabWidget, QGridLayout, QFrame, QColorDialog, QStatusBar, QScrollArea, QMenuBar, QDockWidget, QTextEdit
from PyQt5.QtGui import QFont, QIcon, QPixmap, QTextCharFormat
from PyQt5.QtCore import Qt
from CustomTextEdit import CustomTextEdit
from PagedTextEdit import PagedTextEdit
from actions import TextEditorActions
from menubar import create_menu
from MegaMenuTabs import MegaMenu


class ClickableLabel(QLabel):
    def __init__(self, icon_path, callback, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap(icon_path).scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.callback = callback

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.callback()


class MainWindow(QMainWindow):
    def __init__(self, new_instance_callback=None):
        super().__init__()

        self.setWindowTitle('Fuünda')
        self.setGeometry(100, 100, 1200, 800)

        icon_dir = os.path.join(os.path.dirname(__file__), 'icons')
        self.setWindowIcon(QIcon(os.path.join(icon_dir, 'app-icon.png')))
        self.setWindowTitle('Fuünda')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        central_widget.setStyleSheet("background-color: #f0f0f0;")

        self.create_tabs(main_layout)

        control_widget = QWidget()
        control_layout = QHBoxLayout(control_widget)

        vertical_center_layout = QVBoxLayout()
        main_layout.addLayout(vertical_center_layout)
        vertical_center_layout.addStretch(1)

        center_layout = QHBoxLayout()
        vertical_center_layout.addLayout(center_layout)
        vertical_center_layout.addStretch(1)

        self.textEdit = CustomTextEdit()
        center_layout.addStretch(1)
        center_layout.addWidget(self.textEdit)
        center_layout.addStretch(1)

        self.actions = TextEditorActions(self, new_instance_callback)
        self.create_toolbar()
        create_menu(self)

        self.create_status_bar()

    def create_tabs(self, main_layout):
        tabs = QTabWidget()

        tab_bar_height = 50
        tab_bar_width = 150
        tab_bar_font_size = 14
        tabs.setStyleSheet(f"""
                QTabBar::tab {{
                    height: {tab_bar_height}px;
                    width: {tab_bar_width}px;
                    font-size: {tab_bar_font_size}px;
                }}
                QTabBar::tab:selected {{
                    background: #F9F9F9;
                }}
            """)

        main_layout.addWidget(tabs)

        home_tab = QWidget()
        insertion_tab = QWidget()
        design_tab = QWidget()
        page_layout_tab = QWidget()
        reference_tab = QWidget()
        revision_tab = QWidget()
        view_tab = QWidget()
        help_tab = QWidget()

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
        home_tab.setLayout(home_layout)

        # Set background color for the active tab body
        home_tab.setStyleSheet("background: #F9F9F9;")
        insertion_tab.setStyleSheet("background: #F9F9F9;")
        design_tab.setStyleSheet("background: #F9F9F9;")
        page_layout_tab.setStyleSheet("background: #F9F9F9;")
        reference_tab.setStyleSheet("background: #F9F9F9;")
        revision_tab.setStyleSheet("background: #F9F9F9;")
        view_tab.setStyleSheet("background: #F9F9F9;")
        help_tab.setStyleSheet("background: #F9F9F9;")

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

        # Create container widgets for the layouts
        text_container = QWidget()
        text_container.setLayout(text_layout)

        align_container = QWidget()
        align_container.setLayout(align_layout)

        style_container = QWidget()
        style_container.setLayout(style_layout)

        # Add containers to a horizontal layout
        h_layout = QHBoxLayout()
        h_layout.addWidget(text_container)
        h_layout.addWidget(align_container)
        h_layout.addWidget(style_container)

        # Set the stretch factors to make each container take 33% of the space
        h_layout.setStretch(0, 1)
        h_layout.setStretch(1, 1)
        h_layout.setStretch(2, 1)

        # Add the horizontal layout to the main layout
        home_layout.addLayout(h_layout, 0, 0)

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

        # Add the QSlider for zoom functionality to the home_layout
        self.zoom_slider = QSlider(Qt.Horizontal)
        self.zoom_slider.setMinimum(-10)  # Minimum zoom level
        self.zoom_slider.setMaximum(10)  # Maximum zoom level
        self.zoom_slider.setValue(0)  # Start at the middle point
        self.zoom_slider.setTickPosition(QSlider.TicksBelow)
        self.zoom_slider.setTickInterval(1)
        self.zoom_slider.valueChanged.connect(self.handle_zoom)

        # Set a fixed width for the QSlider
        self.zoom_slider.setFixedWidth(self.width() // 4)

        home_layout.addWidget(self.zoom_slider, 1, 0, 1, 1)  # Adjust this to position the slider as needed

        self.font_combo = QComboBox()
        self.font_combo.addItems(sorted([
            "Arial", "Arial Black", "Comic Sans MS", "Courier New", "Georgia",
            "Impact", "Lucida Console", "Lucida Sans Unicode", "Palatino Linotype",
            "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana", "Baskerville",
            "Cambria", "Courier", "Garamond", "calibri", "Century Gothic",
            "DejaVu Sans", "Copperplate", "Brush Script M7", "Roboto", "Monserrat",
            "Consolas", "Goudy Old Style", "Helvetica", "Lucida Bright", "Lucida Sans",
            "Palatino", "Optima", "Rockwell", "Perpetua", "Segoe UI"
        ]))
        self.font_combo.currentIndexChanged.connect(self.update_labels_font)
        home_layout.addWidget(self.font_combo, 1, 1, 1, 1)
        # control_layout.addWidget(self.font_combo)

        self.size_spinbox = QSpinBox()
        self.size_spinbox.setValue(12)
        self.size_spinbox.valueChanged.connect(self.update_labels_size)
        home_layout.addWidget(self.size_spinbox, 1, 2, 1, 1)

        # Create layout for the page navigation controls
        self.paged_text_layout = QHBoxLayout()
        self.pagedTextEdit = PagedTextEdit()

        # Adjust button size to fit the text
        self.pagedTextEdit.prev_button.setFixedSize(self.pagedTextEdit.prev_button.sizeHint())
        self.pagedTextEdit.next_button.setFixedSize(self.pagedTextEdit.next_button.sizeHint())

        # Add buttons and label to layout
        self.paged_text_layout.addWidget(self.pagedTextEdit.prev_button)
        self.paged_text_layout.addWidget(self.pagedTextEdit.page_label)
        self.paged_text_layout.addWidget(self.pagedTextEdit.next_button)

        self.paged_text_layout.addStretch()  # Push the controls to the left

        home_layout.addLayout(self.paged_text_layout, 2, 0, 1, 3)  # Add the navigation controls layout to home_layout

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

    # Texte barré
    def set_strikethrough(self):
        font = self.textEdit.font()
        font.setStrikeOut(not font.strikeOut())
        self.textEdit.setFont(font)

    def set_index(self):  # Texte en indice
        char_format = QTextCharFormat()
        cursor = self.textEdit.textCursor()
        char_format.setVerticalAlignment(QTextCharFormat.AlignSubScript)
        cursor.mergeCharFormat(char_format)

    # Texte en exposant
    def set_superscript(self):
        char_format = QTextCharFormat()
        cursor = self.textEdit.textCursor()
        char_format.setVerticalAlignment(QTextCharFormat.AlignSuperScript)
        cursor.mergeCharFormat(char_format)

    # Implement color application logic
    def apply_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            char_format = QTextCharFormat()
            char_format.setForeground(color)
            cursor = self.textEdit.textCursor()
            cursor.mergeCharFormat(char_format)

    # Implement highlight application logic
    def apply_highlight(self):
        color = QColorDialog.getColor()
        if color.isValid():
            char_format = QTextCharFormat()
            char_format.setBackground(color)
            cursor = self.textEdit.textCursor()
            cursor.mergeCharFormat(char_format)

    def handle_zoom(self, value):
        font = self.textEdit.font()
        base_size = 12
        font.setPointSize(base_size + value)
        self.textEdit.setFont(font)
        a4_base_width = int(210 * 3.78)
        new_width = a4_base_width + value * 20
        self.textEdit.setFixedWidth(new_width)

    def create_toolbar(self):
        self.toolbar = QToolBar("Main Toolbar")
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

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

    def create_status_bar(self):
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        status_bar_border = "0px groove #f0f0f0"
        status_bar_height = 20
        status_bar_bckg = "#f9f9f9"

        self.statusBar.addPermanentWidget(QLabel("Ready"))
        self.statusBar.showMessage("Ready")
        self.statusBar.setStyleSheet(f"""
            QStatusBar {{
                border: {status_bar_border}; 
                height: {status_bar_height}px; 
                background: {status_bar_bckg};
                color: #666666;
                font-size: 12px;
                font-weight: bold;
                padding: 2px 5px 2px 5px;
            }}
            QStatusBar QLabel {{
                padding-left: 5px;
                padding-right: 5px;
            }}""")

    def create_dock_widgets(self):
        self.dock_widgets = QDockWidget("Dock Widgets")
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_widgets)
        self.dock_widgets.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dock_widgets.setWidget(QTextEdit())
        self.dock_widgets.setFeatures(QDockWidget.DockWidgetMovable)

    def create_tool_bar(self):
        self.toolbar = QToolBar()

    def create_menu_bar(self):
        self.menubar = QMenuBar(self)
        self.setMenuBar(self.menubar)

        self.fileMenu = self.menubar.addMenu("File")
