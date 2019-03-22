import numpy as np




 

class Stratec():
	def __init__(self):
		self.matrix = None
			

	def loadCSV(self, path):
		self.matrix = np.genfromtxt(path,delimiter=',')
	
	def getMatrix(self):
		return self.matrix

       ##################################################################	Level 1
       #         							#   
	
	def lee(self):
		pass
		
	
	def levelOne(self):
		self.loadCSV('The_Basics.csv')	
		
		shape = self.matrix.shape
		wM = shape[1]
		hM = shape[0]		

		
				
		

	

       #								 #
       ###################################################################


str = Stratec()
str.levelOne()