from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QAction, QFileDialog, QMessageBox
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtGui import QIcon
import os


class TextEditorActions:
    def __init__(self, parent, new_instance_callback=None):
        self.parent = parent
        self.new_instance_callback = new_instance_callback
        self.icon_dir = os.path.join(os.path.dirname(__file__), 'icons')
        self.currentFile = None

        self.newAction = QAction(QIcon(os.path.join(self.icon_dir, 'new-24x24.png')), 'New', parent)
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.triggered.connect(self.newFile)

        self.openAction = QAction(QIcon(os.path.join(self.icon_dir, 'open-24x24.png')), 'Open', parent)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.triggered.connect(self.openFile)

        self.saveAction = QAction(QIcon(os.path.join(self.icon_dir, 'save-24x24.png')), 'Save', parent)
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.triggered.connect(self.saveFile)

        self.saveAsAction = QAction('Save As', parent)
        self.saveAsAction.setShortcut('Ctrl+Shift+S')
        self.saveAsAction.triggered.connect(self.saveFileAs)

        self.closeAction = QAction(QIcon(os.path.join(self.icon_dir, 'close-24x24.png')), 'Close', parent)
        self.closeAction.setShortcut('Ctrl+W')
        self.closeAction.triggered.connect(self.closeFile)

        self.printAction = QAction(QIcon(os.path.join(self.icon_dir, 'print-24x24.png')), 'Print', parent)
        self.printAction.setShortcut('Ctrl+P')
        self.printAction.triggered.connect(self.printFile)

        self.exitAction = QAction(QIcon(os.path.join(self.icon_dir, 'exit-24x24.png')), 'Exit', parent)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.triggered.connect(parent.close)

        self.cutAction = QAction(QIcon(os.path.join(self.icon_dir, 'cut-24x24.png')), 'Cut', parent)
        self.cutAction.setShortcut('Ctrl+X')
        self.cutAction.triggered.connect(parent.textEdit.cut)

        self.copyAction = QAction(QIcon(os.path.join(self.icon_dir, 'copy-24x24.png')), 'Copy', parent)
        self.copyAction.setShortcut('Ctrl+C')
        self.copyAction.triggered.connect(parent.textEdit.copy)

        self.pasteAction = QAction(QIcon(os.path.join(self.icon_dir, 'paste-24x24.png')), 'Paste', parent)
        self.pasteAction.setShortcut('Ctrl+V')
        self.pasteAction.triggered.connect(parent.textEdit.paste)

        self.undoAction = QAction(QIcon(os.path.join(self.icon_dir, 'undo-24x24.png')), 'Undo', parent)
        self.undoAction.setShortcut('Ctrl+Z')
        self.undoAction.triggered.connect(parent.textEdit.undo)

        self.redoAction = QAction(QIcon(os.path.join(self.icon_dir, 'redo-24x24.png')), 'Redo', parent)
        self.redoAction.setShortcut('Ctrl+Y')
        self.redoAction.triggered.connect(parent.textEdit.redo)

        self.aboutAction = QAction('About', parent)
        self.aboutAction.triggered.connect(self.about)

    def newFile(self):
        if self.new_instance_callback:
            self.new_instance_callback()

    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self.parent, "Open File", "", "All Files (*);;Text Files (*.txt)",
                                                  options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.parent.textEdit.setText(file.read())
            self.currentFile = fileName
            self.parent.setWindowTitle(f'Funda - {fileName}')

    def saveFile(self):
        if self.currentFile:
            with open(self.currentFile, 'w') as file:
                file.write(self.parent.textEdit.toPlainText())
        else:
            self.saveFileAs()

    def saveFileAs(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self.parent, "Save File", "", "All Files (*);;Text Files (*.txt)",
                                                  options=options)
        if fileName:
            self.currentFile = fileName
            with open(fileName, 'w') as file:
                file.write(self.parent.textEdit.toPlainText())
            self.parent.setWindowTitle(f'Funda - {fileName}')

    def closeFile(self):
        self.parent.textEdit.clear()
        self.parent.setWindowTitle('Funda')

    def printFile(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self.parent)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.parent.textEdit.print_(printer)

    def about(self):
        QMessageBox.about(self.parent, "About", "Ceci est une application de traitement de texte créée avec PyQt.")

'''
class ActionHandler:
    newFileTriggered = pyqtSignal()
    closeFileTriggered = pyqtSignal()
    printFileTriggered = pyqtSignal()
'''