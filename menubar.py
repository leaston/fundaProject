def create_menu(parent):
    actions = parent.actions

    menubar = parent.menuBar()

    fileMenu = menubar.addMenu('File')
    fileMenu.addAction(actions.newAction)
    fileMenu.addAction(actions.openAction)
    fileMenu.addAction(actions.saveAction)
    fileMenu.addAction(actions.saveAsAction)
    fileMenu.addSeparator()
    fileMenu.addAction(actions.closeAction)
    fileMenu.addAction(actions.printAction)
    fileMenu.addSeparator()
    fileMenu.addAction(actions.exitAction)

    editMenu = menubar.addMenu('Edit')
    editMenu.addAction(actions.cutAction)
    editMenu.addAction(actions.copyAction)
    editMenu.addAction(actions.pasteAction)
    editMenu.addSeparator()
    editMenu.addAction(actions.undoAction)
    editMenu.addAction(actions.redoAction)

    helpMenu = menubar.addMenu('Help')
    helpMenu.addAction(actions.aboutAction)

    return menubar
