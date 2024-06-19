import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.initUI()

    def initUI(self):
        newAction = QAction(QIcon('new.png'), 'New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.newFile)

        openAction = QAction(QIcon('open.png'), 'Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openFile)

        saveAction = QAction(QIcon('save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Text Editor')
        self.show()

    def newFile(self):
        self.textEdit.clear()

    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)",
                                                  options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.textEdit.setText(file.read())

    def saveFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Text Files (*.txt)",
                                                  options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textEdit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec_())
