from PyQt5 import QtWidgets, uic 
import sys 
import numpy as np 

class MainWindow(QtWidgets.QMainWindow): 
	
	def __init__(self, *args, **kwargs): 
		super(MainWindow, self).__init__(*args, **kwargs) 
		# Load the UI Page 
		self. ui = uic.loadUi('mainwindow.ui', self) 
		# Create a sin wave 
		x_time = np.arange(0, 100, 0.1); 
		y_amplitude = np.sin(x_time) 
		
		pltSignal = self.widgetSignal 
		pltSignal.clear() 
		pltSignal.setLabel('left', 'Signal Sin Wave', units ='(V)') 
		pltSignal.setLabel('bottom', 'Time', units ='(sec)') 
		pltSignal.plot(x_time, y_amplitude, clear = True) 

		self.ui.show() 

def main(): 
	app = QtWidgets.QApplication(sys.argv) 
	window = MainWindow() 
	sys.exit(app.exec_()) 

if __name__ == '__main__': 
	main()	 

