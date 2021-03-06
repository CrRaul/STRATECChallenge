import numpy as np
from queue import Queue
import random

class Stratec():
	def __init__(self):
		self.matrix = None
		self.solLvl1 = None	
		self.solLvl2 = None		
		self.path = None

	def loadCSV(self, path):
		self.matrix = np.genfromtxt(path,delimiter=',')
	
	def getMatrix(self):
		return self.matrix

	
	def fill(self, start, colorList, color = None):
		q = Queue()
		q.put(start)

		if color == None:
			color = random.randint(190,255)
			while color in colorList:
				color = random.randint(190,255)

		self.matrix[start[0],start[1]] = color

		while not q.empty():
			index = q.get()	
			
			l = (index[0], index[1]-1)
			r = (index[0], index[1]+1)
			u = (index[0]-1, index[1])
			d = (index[0]+1, index[1])


			if l[1] >= 0 and self.matrix[l[0]][l[1]] == 3:
				q.put(l)
				self.matrix[l[0],l[1]] = color				
						

			if r[1] < len(self.matrix[0]) and self.matrix[r[0]][r[1]] == 3:
				q.put(r)
				self.matrix[r[0],r[1]] = color


			if u[0] >= 0 and self.matrix[u[0]][u[1]] == 3:
				q.put(u)
				self.matrix[u[0],u[1]] = color


			if d[0] < len(self.matrix) and self.matrix[d[0]][d[1]] == 3:
				q.put(d)
				self.matrix[d[0],d[1]] = color
		return color	

       ##################################################################	Level 1
       #         							#   
	def checkMarkNoise(self, start):
		q = Queue()
		q.put(start)
		
		stepDirections = [0,0,0,0]		
		direction = []

		self.matrix[start[0],start[1]] = 2

		while not q.empty():
			index = q.get()	
			
			l = (index[0], index[1]-1)
			r = (index[0], index[1]+1)
			u = (index[0]-1, index[1])
			d = (index[0]+1, index[1])


			if l[1] >= 0 and self.matrix[l[0]][l[1]] == 1:

				stepDirections[0] += 1 
				direction.append(0)
				q.put(l)
				self.matrix[l[0],l[1]] = 2				
						

			if r[1] < len(self.matrix[0]) and self.matrix[r[0]][r[1]] == 1:

				stepDirections[1] += 1
				direction.append(1)
				q.put(r)
				self.matrix[r[0],r[1]] = 2


			if u[0] >= 0 and self.matrix[u[0]][u[1]] == 1:

				stepDirections[2] += 1
				direction.append(2)
				q.put(u)
				self.matrix[u[0],u[1]] = 2

			if d[0] < len(self.matrix) and self.matrix[d[0]][d[1]] == 1:

				stepDirections[3] += 1
				direction.append(3)
				q.put(d)
				self.matrix[d[0],d[1]] = 2


		num = 0
		for i in range(4):
			if stepDirections[i] >= 1:
				num += 1

		if num == 1 or num == 0:
			self.matrix[start[0],start[1]] = -1
			for i in range(len(direction)):
				if direction[i] == 0:
					start = (start[0], start[1] - 1) 

				if direction[i] == 1: 
					start = (start[0], start[1] + 1) 

				if direction[i] == 2: 
					start = (start[0] - 1, start[1]) 

				if direction[i] == 3: 
					start = (start[0] + 1, start[1]) 
				self.matrix[start[0],start[1]] = -1
			return True
		return False
				
	
	def levelOne(self):
		if self.path != 3:
			self.loadCSV('input/The_Basics.csv')	

		shape = self.matrix.shape
		wM = shape[1]
		hM = shape[0]		
		
		numNoise = numTotalS = 0
		
		for i in range(hM):
			for j in range(wM):
				if self.matrix[i][j] == 1:
					if self.checkMarkNoise((i,j)) == True:	
						numNoise += 1
					numTotalS +=1
		#self.checkMarkNoise((9,18))	

		if self.path!=3:
			# write the solution into file			
			text_file = open("sol/lvl1.txt", "w")
			text_file.write(str(numTotalS-numNoise))
			text_file.close()
			self.solLvl1 = numTotalS-numNoise

		return numTotalS-numNoise
       #								 #
       ###################################################################



	##################################################################	Level 2
       #         							#   
	def checkMarkBox(self, start):
		q = Queue()
		q.put(start)
		
		xMin, yMin = 100,100
		xMax, yMax = -1,-1

		self.matrix[start[0],start[1]] = 3

		while not q.empty():
			index = q.get()	
			
			l = (index[0], index[1]-1)
			r = (index[0], index[1]+1)
			u = (index[0]-1, index[1])
			d = (index[0]+1, index[1])

			if index[1] < xMin:
				xMin = index[1]			
			if index[1] > xMax:
				xMax = index[1]
			if index[0] < yMin:
				yMin = index[0]				
			if index[0] > yMax:
				yMax = index[0]

			if l[1] >= 0 and self.matrix[l[0]][l[1]] == 2:
				q.put(l)
				self.matrix[l[0],l[1]] = 3				
						

			if r[1] < len(self.matrix[0]) and self.matrix[r[0]][r[1]] == 2:
				q.put(r)
				self.matrix[r[0],r[1]] = 3


			if u[0] >= 0 and self.matrix[u[0]][u[1]] == 2:
				q.put(u)
				self.matrix[u[0],u[1]] = 3


			if d[0] < len(self.matrix) and self.matrix[d[0]][d[1]] == 2:
				q.put(d)
				self.matrix[d[0],d[1]] = 3
	
	
		if xMin == xMax and yMin == yMax: 
			return [0,0,0,0]

		return [xMin,yMin,xMax,yMax]
	
	def levelTwo(self):
		if self.path != 3:
			self.loadCSV('input/The_Basics.csv')

		self.solLvl1 = self.levelOne()
	
		shape = self.matrix.shape
		wM = shape[1]
		hM = shape[0]		
		
		sol = []
		
		for i in range(hM):
			for j in range(wM):
				if self.matrix[i][j] == 2:
					s = self.checkMarkBox((i,j))

					if s[0] == 0 and s[1] == 0 and s[2] == 0 and s[3] == 0:
						continue
					else:
						sol.append(s)	
		if self.path!=3:
			# write the solution into file		
			text_file = open("sol/lvl2.txt", "w")
			text_file.write(str(self.solLvl1)+"\n")

			for i in range(len(sol)):
				xL = sol[i][0]
				yL = sol[i][1]        
				xR = sol[i][2]
				yR = sol[i][3]
			
				text_file.write("("+str(yL)+","+str(xL)+") W:"+str(xR-xL+1)+" H:"+str(yR-yL+1)+"\n")
	
			text_file.close()

		self.path = None
		return sol
       #								 #
       ###################################################################


       ##################################################################	Level 3
       #         							#   
	def checkEquMatrix(self, posM1, posM2):
		A = self.matrix[posM1[1]:posM1[3]+1,posM1[0]:posM1[2]+1]
		B = self.matrix[posM2[1]:posM2[3]+1,posM2[0]:posM2[2]+1]
		
		if np.array_equal(A, B):
			return True

		return False
		

	def levelThree(self):

		self.loadCSV('input/Duplicates.csv')
		self.path = 3
		self.solLvl2 = self.levelTwo()
	
		sol = self.solLvl2	
		
		# write the solution into file		
		text_file = open("sol/lvl3.txt", "w")
		text_file.write(str(self.solLvl1)+"\n")
		
		colorList = []		
		
		for i in range(len(sol)):
			if sol[i][0]!=-1:			
				dupList = []
				for j in range(i+1,len(sol)):
					ok =  self.checkEquMatrix(sol[i],sol[j])
					if ok == True:
						dupList.append(j)

				xL = sol[i][0]
				yL = sol[i][1]        
				xR = sol[i][2]
				yR = sol[i][3]

			
				if len(dupList) == 0:	
					text_file.write("("+str(yL)+","+str(xL)+") W:"+str(xR-xL+1)+" H:"+str(yR-yL+1)+"\n")
				else:
					color = self.fill((sol[i][1],sol[i][0]),colorList)
					colorList.append(color)


					text_file.write("("+str(yL)+","+str(xL)+") W:"+str(xR-xL+1)+" H:"+str(yR-yL+1))
								
					for k in range(len(dupList)):			
						xL2 = sol[dupList[k]][0]
						yL2 = sol[dupList[k]][1]
	
						color = self.fill((sol[dupList[k]][1],sol[dupList[k]][0]),colorList, color)				
						if k == 0:
							text_file.write("- this object is also found at "+"("+str(yL2)+","+str(xL2)+")")
						else:
							text_file.write(", and at "+"("+str(yL2)+","+str(xL2)+")")
						sol[dupList[k]][0] = -1
						sol[dupList[k]][1] = -1
						sol[dupList[k]][2] = -1
						sol[dupList[k]][3] = -1
					text_file.write("\n")

		text_file.close()
       #								 #
       ###################################################################
	

	##################################################################	Level 4
       #         							#   
	def checkEquMatrix4(self, posM1, posM2):
		A = self.matrix[posM1[1]:posM1[3]+1,posM1[0]:posM1[2]+1]
		B = self.matrix[posM2[1]:posM2[3]+1,posM2[0]:posM2[2]+1]

		angle = 0

		for k in range(4):

			if np.array_equal(A, B):
				return [True, angle]
			
			angle += 90
			B = np.rot90(B,-1)


		return [False,None]
		
		

	def levelFour(self):

		self.loadCSV('input/Duplicates_Advanced.csv')
		self.path = 3
		self.solLvl2 = self.levelTwo()
	
		sol = self.solLvl2	
		
		# write the solution into file		
		text_file = open("sol/lvl4.txt", "w")
		text_file.write(str(self.solLvl1)+"\n")
		
		colorList = []		
		
		for i in range(len(sol)):
			if sol[i][0] != -1:
				dupList = []
				angleDup = []
				for j in range(i+1,len(sol)):
					solEqu = self.checkEquMatrix4(sol[i],sol[j])
					if solEqu[0]:
						dupList.append(j)
						angleDup.append(solEqu[1])
					
				xL = sol[i][0]
				yL = sol[i][1]        
				xR = sol[i][2]
				yR = sol[i][3]

				if len(dupList) == 0:	
					text_file.write("\n")
					text_file.write("("+str(yL)+","+str(xL)+") W:"+str(xR-xL+1)+" H:"+str(yR-yL+1).rstrip('\n'))
				else:
					
					color = self.fill((sol[i][1],sol[i][0]),colorList)
					colorList.append(color)
					text_file.write("\n")
					text_file.write("("+str(yL)+","+str(xL)+") W:"+str(xR-xL+1)+" H:"+str(yR-yL+1).rstrip('\n'))
					for k in range(len(dupList)):
						if sol[dupList[k]][0] != -1:				
							xL2 = sol[dupList[k]][0]
							yL2 = sol[dupList[k]][1]
		
							color = self.fill((sol[dupList[k]][1],sol[dupList[k]][0]),colorList, color)				
							if k == 0:
								text_file.write("- this object is also found at "+"("+str(yL2)+","+str(xL2)+")"+ ", rotated by "+str(angleDup[k])+ " degrees".rstrip('\n'))
							else:
								text_file.write(", and at "+"("+str(yL2)+","+str(xL2)+")"+ ", rotated by "+str(angleDup[k])+ " degrees".rstrip('\n'))
							sol[dupList[k]][0] = -1
				
		text_file.close()
       #								 #
       ###################################################################
