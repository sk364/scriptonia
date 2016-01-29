#!/usr/bin/python

import sys
from PyQt4 import QtGui
import pygame

pygame.mixer.init()

class MusicPlayer(QtGui.QMainWindow):
    
    	def __init__(self):
        	super(MusicPlayer, self).__init__()
        
        	self.initUI()
        
    	def initUI(self):
		

		menubar = self.menuBar()
		self.fileMenu = menubar.addMenu('&File')
		#self.editMenu = menubar.addMenu('&Edit')
		self.viewMenu = menubar.addMenu('&View')

		self.initFileMenuActions()
                #self.initEditMenuActions()
		self.initViewMenuActions()
		# TODO add view and tools menubar


		self.setGeometry(100, 100, 800, 600)
		self.setWindowTitle('Music Player')

		self.show()

	def initFileMenuActions(self):
		'''newFile = QtGui.QAction(QtGui.QIcon('new.png'), 'New', self)
                newFile.setShortcut('Ctrl+N')
                newFile.setStatusTip('New file')
                newFile.triggered.connect(self.new_file)
		
		toolbar = self.addToolBar('New')
        	toolbar.addAction(newFile)'''

                openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
                openFile.setShortcut('Ctrl+O')
                openFile.setStatusTip('Open new File')
                openFile.triggered.connect(self.open_file)

                #toolbar.addAction(openFile)

                exitPlayer = QtGui.QAction(QtGui.QIcon('exit24.png'),'Exit',self)
                exitPlayer.setShortcut('Ctrl+W')
                exitPlayer.setStatusTip('Exit')
                exitPlayer.triggered.connect(self.exit)

                #toolbar.addAction(exitFile)

                self.fileMenu.addAction(openFile)
                self.fileMenu.addAction(exitPlayer)


        def initViewMenuActions(self):
                statusBar= QtGui.QAction(QtGui.QIcon('status.png'), 'Status Bar', self)
                statusBar.setStatusTip('Status Bar')
                #statusBar.triggered.connect(
		#QStatusBar.addWidget (self, QWidget widget, int stretch = 0)
		#)

		self.viewMenu.addAction(statusBar)



    	def open_file(self):
        	fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')        
		print fname
       		#f = open(fname, 'r')
        
        	if fname:        
			pygame.mixer.music.load(str(fname))
			pygame.mixer.music.play()


	def exit(self):
		sys.exit()


def main():
   	app = QtGui.QApplication(sys.argv)
    	editor = MusicPlayer()
    	sys.exit(app.exec_())


if __name__ == '__main__':	main()
