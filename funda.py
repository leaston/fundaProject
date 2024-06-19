import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Funda')

        # Actions
        newAction = QAction(QIcon('icons/new.png'), 'New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.newFile)

        openAction = QAction(QIcon('icons/open.png'), 'Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openFile)

        saveAction = QAction(QIcon('icons/save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)

        saveAsAction = QAction('Save As', self)
        saveAsAction.setShortcut('Ctrl+Shift+S')
        saveAsAction.triggered.connect(self.saveFileAs)

        closeAction = QAction(QIcon('icons/close.png'), 'Close', self)
        closeAction.setShortcut('Ctrl+W')
        closeAction.triggered.connect(self.closeFile)

        printAction = QAction(QIcon('icons/print.png'), 'Print', self)
        printAction.setShortcut('Ctrl+P')
        printAction.triggered.connect(self.printFile)

        exitAction = QAction(QIcon('icons/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)

        cutAction = QAction(QIcon('icons/cut.png'), 'Cut', self)
        cutAction.setShortcut('Ctrl+X')
        cutAction.triggered.connect(self.textEdit.cut)

        copyAction = QAction(QIcon('icons/copy.png'), 'Copy', self)
        copyAction.setShortcut('Ctrl+C')
        copyAction.triggered.connect(self.textEdit.copy)

        pasteAction = QAction(QIcon('icons/paste.png'), 'Paste', self)
        pasteAction.setShortcut('Ctrl+V')
        pasteAction.triggered.connect(self.textEdit.paste)

        undoAction = QAction(QIcon('icons/undo.png'), 'Undo', self)
        undoAction.setShortcut('Ctrl+Z')
        undoAction.triggered.connect(self.textEdit.undo)

        redoAction = QAction(QIcon('icons/redo.png'), 'Redo', self)
        redoAction.setShortcut('Ctrl+Y')
        redoAction.triggered.connect(self.textEdit.redo)

        aboutAction = QAction('About', self)
        aboutAction.triggered.connect(self.about)

        # Menubar
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addSeparator()
        fileMenu.addAction(closeAction)
        fileMenu.addAction(printAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        editMenu = menubar.addMenu('Edit')
        editMenu.addAction(cutAction)
        editMenu.addAction(copyAction)
        editMenu.addAction(pasteAction)
        editMenu.addSeparator()
        editMenu.addAction(undoAction)
        editMenu.addAction(redoAction)

        helpMenu = menubar.addMenu('Help')
        helpMenu.addAction(aboutAction)

        # Toolbar
        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(newAction)
        toolbar.addAction(openAction)
        toolbar.addAction(saveAction)
        toolbar.addSeparator()
        toolbar.addAction(cutAction)
        toolbar.addAction(copyAction)
        toolbar.addAction(pasteAction)
        toolbar.addSeparator()
        toolbar.addAction(undoAction)
        toolbar.addAction(redoAction)

        self.setGeometry(300, 300, 800, 600)
        self.show()

    def newFile(self):
        new_instance = TextEditor()
        new_instance.show()

    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)",
                                                  options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.textEdit.setText(file.read())
            self.currentFile = fileName
            self.setWindowTitle(f'Mon Application de Traitement de Texte - {fileName}')

    def saveFile(self):
        if hasattr(self, 'currentFile') and self.currentFile:
            with open(self.currentFile, 'w') as file:
                file.write(self.textEdit.toPlainText())
        else:
            self.saveFileAs()

    def saveFileAs(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Text Files (*.txt)",
                                                  options=options)
        if fileName:
            self.currentFile = fileName
            with open(fileName, 'w') as file:
                file.write(self.textEdit.toPlainText())
            self.setWindowTitle(f'Mon Application de Traitement de Texte - {fileName}')

    def closeFile(self):
        self.textEdit.clear()
        self.setWindowTitle('Mon Application de Traitement de Texte')

    def printFile(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def about(self):
        QMessageBox.about(self, "About", "Ceci est une application de traitement de texte créée avec PyQt.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec_())
