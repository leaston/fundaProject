import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QToolBar, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon


class MegaMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Mega Menu Example')
        self.setGeometry(100, 100, 800, 600)

        self.create_menus()
        self.create_toolbar()

        # Central widget
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def create_menus(self):
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu('File')
        new_action = QAction('New', self)
        open_action = QAction('Open', self)
        save_action = QAction('Save', self)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        # Edit menu
        edit_menu = menubar.addMenu('Edit')
        cut_action = QAction('Cut', self)
        copy_action = QAction('Copy', self)
        paste_action = QAction('Paste', self)

        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)

        # View menu with a sub-menu
        view_menu = menubar.addMenu('View')
        zoom_menu = QMenu('Zoom', self)
        zoom_in_action = QAction('Zoom In', self)
        zoom_out_action = QAction('Zoom Out', self)

        zoom_menu.addAction(zoom_in_action)
        zoom_menu.addAction(zoom_out_action)
        view_menu.addMenu(zoom_menu)

    def create_toolbar(self):
        toolbar = (QToolBar('Main Toolbar'))
        self.addToolBar(toolbar)

        # Set toolbar height
        toolbar.setFixedHeight(100)

        new_action = QAction(QIcon(None), 'New', self)
        open_action = QAction(QIcon(None), 'Open', self)
        save_action = QAction(QIcon(None), 'Save', self)
        cut_action = QAction(QIcon(None), 'Cut', self)
        copy_action = QAction(QIcon(None), 'Copy', self)
        paste_action = QAction(QIcon(None), 'Paste', self)

        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)
        toolbar.addSeparator()
        toolbar.addAction(cut_action)
        toolbar.addAction(copy_action)
        toolbar.addAction(paste_action)

        # Add a label to the toolbar
        toolbar.addSeparator()
        toolbar.addWidget(QLabel('Toolbar Example'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MegaMenu()
    window.show()
    sys.exit(app.exec_())
