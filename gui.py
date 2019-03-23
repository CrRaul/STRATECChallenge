from Stratec import *

from tkinter import *
import tkinter as tki
from PIL import ImageTk, Image
import cv2

import numpy as np

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)   

        self.stratec = Stratec()	

        self.image = None
        self.panel = None
        
	#reference to the master widget, which is the tk window                 
        self.master = master

        self.iW = 950
        self.iH = 450
	
	# draw the number range ( up - down). Static
        for i in range(self.iH//10):
            w = tki.Label(self.master, text = i)
            w.config(font=("Courier", 6))
            w.pack()
            w.place(x = 10, y = i*10+25)

            w = tki.Label(self.master, text = i)
            w.config(font=("Courier", 6))
            w.pack()
            w.place(x = 980, y = i*10+25)
	
	# draw the number range ( left - right). Static
        for i in range(self.iW//10):
            w = tki.Label(self.master, text = i)
            w.config(font=("Courier", 5))
            w.pack()
            w.place(x = i*10+25, y = 10)
		
            w = tki.Label(self.master, text = i)
            w.config(font=("Courier", 5))
            w.pack()
            w.place(x = i*10+25, y = 480)

        self.init_window()
    #############################################################		LVL 1

    def drawLevelOne(self):
        im = np.zeros((self.iH, self.iW, 3), np.uint8)
	
	# solve lvl 1 and save the result
        sol = self.stratec.levelOne()
	
	# get the modified matrix
        matrix = self.stratec.getMatrix()
	
	# draw the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 2:
                    im[i*10:i*10+10, j*10:j*10+10, 1] = 255           
		
                if matrix[i][j] == -1:
                    im[i*10:i*10+10, j*10:j*10+10, 2] = 255      

                cv2.line(im, (j*10, 0), (j*10, self.iH), (50,50,50), 1)
            cv2.line(im, (0, i*10), (self.iW, i*10), (50,50,50), 1)
        
        
        w = tki.Label(self.master, text = "                Number of non-noise objects: ")
        w.pack()
        w.place(x = 310, y = 495)
	
        w = tki.Label(self.master, text = str(sol)+"                ")
        w.pack()
        w.place(x = 560, y = 495)
	
	
        self.image = im
        self.updatePanel()

    #############################################################    

    #############################################################		LVL 2

    def drawLevelTwo(self):
        im = np.zeros((self.iH, self.iW, 3), np.uint8)
	
	# solve lvl 2 and save the result
        sol = self.stratec.levelTwo()
	
	# get the modified matrix
        matrix = self.stratec.getMatrix()
	
	# draw the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 3:
                    im[i*10:i*10+10, j*10:j*10+10, 1] = 255           
		
                if matrix[i][j] == -1:
                    im[i*10:i*10+10, j*10:j*10+10, 2] = 255      

                cv2.line(im, (j*10, 0), (j*10, self.iH), (50,50,50), 1)
            cv2.line(im, (0, i*10), (self.iW, i*10), (50,50,50), 1)
        
	
        for i in range(len(sol)):
            xL = sol[i][0]*10
            yL = sol[i][1]*10        
            xR = sol[i][2]*10+10
            yR = sol[i][3]*10+10

            cv2.line(im, (xL,yL), (xL,yR), (255,0,0),2)
            cv2.line(im, (xL,yL), (xR,yL), (255,0,0),2)
            cv2.line(im, (xL,yR), (xR,yR), (255,0,0),2)
            cv2.line(im, (xR,yL), (xR,yR), (255,0,0),2)
        
        w = tki.Label(self.master, text = "                Solution is in \"sol/lvl2.txt\"                ")
        w.pack()
        w.place(x = 360, y = 495)
	
	
        self.image = im
        self.updatePanel()

    #############################################################    


    #############################################################		LVL 3

    def drawLevelThree(self):
        im = np.zeros((self.iH, self.iW, 3), np.uint8)
	
	# solve lvl 3
        self.stratec.levelThree()
	
	# get the modified matrix
        matrix = self.stratec.getMatrix()
	
	# draw the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 3:
                    im[i*10:i*10+10, j*10:j*10+10, 1] = 255           
		
                elif matrix[i][j] == -1:
                    im[i*10:i*10+10, j*10:j*10+10, 2] = 255      
                else:
                    im[i*10:i*10+10, j*10:j*10+10, 0] = matrix[i][j]
                    im[i*10:i*10+10, j*10:j*10+10, 2] = matrix[i][j] / ( i + j+1) 

                cv2.line(im, (j*10, 0), (j*10, self.iH), (50,50,50), 1)
            cv2.line(im, (0, i*10), (self.iW, i*10), (50,50,50), 1)
       
        im[0:10,0:10][0],im[0:10,0:10][1],im[0:10,0:10][2] = 0,0,0 

        w = tki.Label(self.master, text = "                Solution is in \"sol/lvl3.txt\"                ")
        w.pack()
        w.place(x = 360, y = 495)
	
	
        self.image = im
        self.updatePanel()

    #############################################################    

    # update the panel with self.image
    # transform cv2 image to tkinter image and show
    def updatePanel(self):
        b,g,r = cv2.split(self.image)
        img = cv2.merge((r,g,b))
        im = Image.fromarray(img)      
        imgtk = ImageTk.PhotoImage(image = im)
        
        self.panelB = Label(self.master, image=imgtk)
        self.panelB.image = imgtk
        self.panelB.pack(side="left", padx=0, pady=0)
        self.panelB.place(x=25, y=25)
    
    def nothing(self):
        return	

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("StratecGUI - Craioveanu Raul")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.master)

        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="lvl1", command=self.drawLevelOne)
        filemenu.add_command(label="lvl2", command=self.drawLevelTwo)
        filemenu.add_command(label="lvl3", command=self.drawLevelThree)
        filemenu.add_command(label="lvl4", command=self.nothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command= self.master.quit)
        menubar.add_cascade(label="opt", menu=filemenu)

        # display the menu
        self.master.config(menu=menubar)
######################################################     ^
    

root = tki.Tk()

root.geometry("1000x520")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  