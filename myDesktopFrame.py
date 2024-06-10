from tkinter import *
from PIL import ImageTk,Image



class myDesktopFrame(Frame):
    """
    This is one the desktop
    it is basically a grid with files(buttons)
    with some files/apps(buttons) placed initially, to avoid unwanted grid behaviour
    
    
    """
    

    def __init__(self,window):
        self.imagePath= "img/background.jpg"
        self.bgImage= Image.open(self.imagePath)
        self.bgPhoto = ImageTk.PhotoImage(self.bgImage)

        
        self.desktop = Frame(window)
        self.desktop.pack(fill="both", expand=True)
        self.desktop.pack_propagate(False)

        super().__init__(self.desktop)
        label1 = Label( self.desktop, image = self.bgPhoto) 
        label1.place(x = 0, y = 0) 
        
        self.fileManegerButton=Button(master=self.desktop,text="FileManager")
        self.notepadButton=Button(master=self.desktop,text="Notepad")
        self.paintButton=Button(master=self.desktop,text="Paint")
        self.internetButton=Button(master=self.desktop,text="Internet")
        self.settingsButton=Button(master=self.desktop,text="Settings")

        self.fileManegerButton.place(x=50,y=50)
        self.notepadButton.place(x=50,y=100)
        self.paintButton.place(x=50,y=150)
        self.internetButton.place(x=50,y=200)
        self.settingsButton.place(x=50,y=250)

        


        


       

        
   
        