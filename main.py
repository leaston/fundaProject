import sys
from PyQt5.QtWidgets import QApplication
from editor import TextEditor
from MainWindow import MainWindow
from actions import TextEditorActions


def create_new_instance():
    new_instance = MainWindow()
    new_instance.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow(new_instance_callback=create_new_instance)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()