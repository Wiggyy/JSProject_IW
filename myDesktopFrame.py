from tkinter import *
from PIL import ImageTk,Image
from myFrameWindow  import myFrameWindow 
from myNotepadFrame  import myNotepadFrame
from myFileManagerFrame import myFileManagerFrame
from myToolBarFrame import myToolBarFrame
from myPaintFrame import myPaintFrame
from myInternetFrame import myInternetFrame


class myDesktopFrame(Frame):

    def __init__(self,window, openApps):
        self.imagePath= "img/background.jpg"
        self.bgImage= Image.open(self.imagePath)
        self.bgPhoto = ImageTk.PhotoImage(self.bgImage)

        self.openApps=openApps

        self.desktop = Frame(window)
        self.desktop.pack(fill="both", expand=True)
        self.desktop.pack_propagate(False)

        super().__init__(self.desktop)

        self.drawWidgets()
        self.toolbar=None

    def doFileManagerAction(self):
        self.openApps.append(myFrameWindow(myFileManagerFrame(self.desktop, (600,400)),"FileManager",self.toolbar,""))

    def doNotepadAction(self):
        self.openApps.append(myFrameWindow(myNotepadFrame(self.desktop, (600,400)),"Notepad",self.toolbar,""))

    def doPaintAction(self):
        self.openApps.append(myFrameWindow(myPaintFrame(self.desktop, (600,400)),"Paint",self.toolbar,""))

    def doInternetAction(self):
        self.openApps.append(myFrameWindow(myInternetFrame(self.desktop, (600,400)),"Internet",self.toolbar,""))

    def addToolBar(self, toolbar):
        self.toolbar = toolbar

    def drawWidgets(self):
        label1 = Label( self.desktop, image = self.bgPhoto) 
        label1.place(x = 0, y = 0) 

        self.fileManegerButton=Button(master=self.desktop,text="FileManager",command=self.doFileManagerAction)
        self.notepadButton=Button(master=self.desktop,text="Notepad",command=self.doNotepadAction)
        self.paintButton=Button(master=self.desktop,text="Paint",command=self.doPaintAction)
        self.internetButton=Button(master=self.desktop,text="Internet",command=self.doInternetAction)

        self.fileManegerButton.place(x=50,y=50)
        self.notepadButton.place(x=50,y=100)
        self.paintButton.place(x=50,y=150)
        self.internetButton.place(x=50,y=200)
        


        


       

        
   
        