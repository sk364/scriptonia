from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class PaintBoard(QtGui.QWidget):
	def __init__(self):
		super(PaintBoard, self).__init__()

		self.cur_pen_width = 1
		self.cur_color = QColor("#000000")
		self.draws = False

		self.qp = QtGui.QPainter()

		self.setAttribute(Qt.WA_PaintOutsidePaintEvent)

		self.qpen = QPen(self.cur_color)
                self.qpen.setWidth(self.cur_pen_width)

		self.setGeometry(100, 100, 400, 400)
	        self.setWindowTitle('Draw text')

		self.menu = QtGui.QMenu()
		quitAction = QtGui.QAction("Quit",self)
		quitAction.triggered.connect(sys.exit)
		self.menu.addAction(quitAction)

		self.show()

	def mousePressEvent(self, e):
		if e.button() == Qt.LeftButton:
			self.qp.begin(self)
			self.draw(e.x(), e.y())
			self.qp.end()
			self.draws = True
		elif e.button() == Qt.RightButton:
			self.menu.show()

	def mouseMoveEvent(self, e):
		if self.draws:
			self.qp.begin(self)
			self.draw(e.x(), e.y())
			self.qp.end()

	def mouseReleaseEvent(self, e):
		self.draws = False

	def draw(self, x, y):
		self.qp.setPen(self.qpen)
		self.qp.drawPoint(x,y)

	def change_color(self, color):
		self.cur_color = "#000000"

	def change_pen_width(self, width):
		self.cur_pen_width = width
		self.qpen.setWidth(self.cur_pen_width)
		
if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)

	pboard = PaintBoard()
	pboard.setMouseTracking(True)

	sys.exit(app.exec_())
