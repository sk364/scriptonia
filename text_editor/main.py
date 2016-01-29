#!/usr/bin/python

import sys
from PyQt4 import QtGui


class Editor(QtGui.QMainWindow):
    
    	def __init__(self):
        	super(Editor, self).__init__()
        
        	self.initUI()
        
    	def initUI(self):
		self.textEdit = QtGui.QTextEdit()
		self.setCentralWidget(self.textEdit)
		#self.statusBar()

		self.cur_file = ''
		self.is_saved = False
		
		self.textEdit.textChanged.connect(self.text_changes)

		menubar = self.menuBar()
		self.fileMenu = menubar.addMenu('&File')
		self.editMenu = menubar.addMenu('&Edit')
		self.viewMenu = menubar.addMenu('&View')

		self.initFileMenuActions()
                self.initEditMenuActions()
		self.initViewMenuActions()
		# TODO add view and tools menubar


		self.setGeometry(100, 100, 800, 600)
		self.setWindowTitle('New file')

		self.show()

	def initFileMenuActions(self):
		newFile = QtGui.QAction(QtGui.QIcon('new.png'), 'New', self)
                newFile.setShortcut('Ctrl+N')
                newFile.setStatusTip('New file')
                newFile.triggered.connect(self.new_file)
		
		toolbar = self.addToolBar('New')
        	toolbar.addAction(newFile)

                openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
                openFile.setShortcut('Ctrl+O')
                openFile.setStatusTip('Open new File')
                openFile.triggered.connect(self.open_file)

                toolbar.addAction(openFile)

                saveAsFile = QtGui.QAction(QtGui.QIcon('saveAs.png'),'Save As',self)
                saveAsFile.setStatusTip('Save As new or existing file')
                saveAsFile.triggered.connect(self.saveAs_file)

                toolbar.addAction(saveAsFile)

                saveFile = QtGui.QAction(QtGui.QIcon('save.png'),'Save',self)
                saveFile.setShortcut('Ctrl+S')
                saveFile.setStatusTip('Save new File')
                saveFile.triggered.connect(self.save_file)

                toolbar.addAction(saveFile)

                exitFile = QtGui.QAction(QtGui.QIcon('exit24.png'),'Exit',self)
                exitFile.setShortcut('Ctrl+W')
                exitFile.setStatusTip('Exit')
                exitFile.triggered.connect(self.exit_file)

                toolbar.addAction(exitFile)

		self.fileMenu.addAction(newFile)
                self.fileMenu.addAction(openFile)
                self.fileMenu.addAction(saveFile)
                self.fileMenu.addAction(saveAsFile)
                self.fileMenu.addAction(exitFile)

	
	def initEditMenuActions(self):
		cutText = QtGui.QAction(QtGui.QIcon('cut.png'), 'Cut', self)
                cutText.setShortcut('Ctrl+X')
                cutText.setStatusTip('Cut Selected Text')
                cutText.triggered.connect(self.textEdit.cut)

                copyText = QtGui.QAction(QtGui.QIcon('copy.png'), 'Copy', self)
                copyText.setShortcut('Ctrl+C')
                copyText.setStatusTip('Copy Selected Text')
                copyText.triggered.connect(self.textEdit.copy)

                pasteText = QtGui.QAction(QtGui.QIcon('paste.png'),'Paste',self)
		pasteText.setShortcut('Ctrl+V')
                pasteText.setStatusTip('Paste Text')
                pasteText.triggered.connect(self.textEdit.paste)

                selectAllText = QtGui.QAction(QtGui.QIcon('sel_all.png'),'Select All',self)
                selectAllText.setShortcut('Ctrl+A')
                selectAllText.setStatusTip('Select All Text')
                selectAllText.triggered.connect(self.textEdit.selectAll)
		
		undoText = QtGui.QAction(QtGui.QIcon('undo.png'), 'Undo', self)
                undoText.setShortcut('Ctrl+Z')
                undoText.setStatusTip('Undo')
                undoText.triggered.connect(self.textEdit.undo)

		redoText = QtGui.QAction(QtGui.QIcon('redo.png'), 'Redo', self)
                redoText.setShortcut('Ctrl+Y')
                redoText.setStatusTip('Redo')
                redoText.triggered.connect(self.textEdit.redo)



		self.editMenu.addAction(cutText)
                self.editMenu.addAction(copyText)
                self.editMenu.addAction(pasteText)
                self.editMenu.addAction(selectAllText)
		self.editMenu.addAction(undoText)
		self.editMenu.addAction(redoText)


        def initViewMenuActions(self):
                statusBar= QtGui.QAction(QtGui.QIcon('status.png'), 'Status Bar', self)
                statusBar.setStatusTip('Status Bar')
                #statusBar.triggered.connect(
		#QStatusBar.addWidget (self, QWidget widget, int stretch = 0)
		#)

		self.viewMenu.addAction(statusBar)

	def get_real_file_name(self, fname):
		s = ''
		for i in range(len(fname)-1,0,-1):
			if fname[i]!='/':
				s+=fname[i]
			else:	break
		return s		

		
	def text_changes(self):
		if self.cur_file:
			self.setWindowTitle(self.get_real_file_name(self.cur_file)+'*')
		else:	self.setWindowTitle('New file*')
		self.is_saved = False

	
	def show_save_exit_dialogBox(self):
		msg_box = QtGui.QMessageBox()

		msg_box.setText('The changes have not been saved')
		msg_box.setInformativeText('Do you want to save the changes ?')
		msg_box.setWindowTitle('Save?')

		save_button = QtGui.QPushButton('&Save')
		cancel_button = QtGui.QPushButton('&Cancel')

		save_button.clicked.connect(self.save_file)
		cancel_button.clicked.connect(sys.exit)

		msg_box.addButton(save_button, QtGui.QMessageBox.AcceptRole)
		msg_box.addButton(cancel_button, QtGui.QMessageBox.AcceptRole)

		msg_box.exec_()


	def new_file(self):
		text = self.textEdit.toPlainText()

		if not self.is_saved and text:
			self.show_save_exit_dialogBox()
		
		self.textEdit.clear()

		self.cur_file = ''
                self.is_saved = False	
		self.setWindowTitle("New file")


    	def open_file(self):
        	fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')        

       		f = open(fname, 'r')
        
        	if f:        
			self.cur_file = fname
            		data = f.read()
 	           	self.textEdit.setText(data)
			self.is_saved = True
			self.cur_file = fname
			self.setWindowTitle(self.get_real_file_name(fname))
 	
	def saveAs_file(self):
		fname = QtGui.QFileDialog.getSaveFileName(self, 'Save As file', '/home', selectedFilter='*.txt')

		text = self.textEdit.toPlainText()

		if fname:
			f = open(fname,'w')
			f.write(text)
			self.is_saved = True
			self.cur_file = fname
			self.setWindowTitle(self.get_real_file_name(fname))
			f.close()
	
	def save_file(self):
		text = self.textEdit.toPlainText()

		if self.cur_file:	fname = open(self.cur_file, 'w')
		elif text:
			self.saveAs_file()
			return
		else:	return
		
		if fname:
			fname.write(text)
			self.is_saved = True
			self.setWindowTitle(self.get_real_file_name(self.cur_file))
			fname.close()


	def exit_file(self):
		text = self.textEdit.toPlainText()

		if self.is_saved or not text:	sys.exit()

		else:
			self.show_save_exit_dialogBox()
			sys.exit()


def main():
   	app = QtGui.QApplication(sys.argv)
    	editor = Editor()
    	sys.exit(app.exec_())


if __name__ == '__main__':	main()
