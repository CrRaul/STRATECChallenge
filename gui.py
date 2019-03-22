from Stratec import *

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import ntpath
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

        self.init_window()
    #############################################################		LVL 1

    def levelOne(self):
        im = np.zeros((self.iH, self.iW, 3), np.uint8)
	
        self.stratec.levelOne()
	
        matrix = self.stratec.getMatrix()
	

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    im[i*10:i*10+10,j*10:j*10+10] = 255
               
                cv2.line(im, (j*10, 0), (j*10, self.iH), (80,80,80), 1)
            cv2.line(im, (0, i*10), (self.iW, i*10), (80,80,80), 1)
        
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
        filemenu.add_command(label="lvl1", command=self.levelOne)
        filemenu.add_command(label="lvl2", command=self.nothing)
        filemenu.add_command(label="lvl3", command=self.nothing)
        filemenu.add_command(label="lvl4", command=self.nothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command= self.master.quit)
        menubar.add_cascade(label="opt", menu=filemenu)

        # display the menu
        self.master.config(menu=menubar)
######################################################     ^
    

root = Tk()

root.geometry("1000x500")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  