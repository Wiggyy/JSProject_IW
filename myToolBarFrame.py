from tkinter import *

class myToolBarFrame(Frame):
    """
    This is one of the "contents" for myFrameWindow
    It consists of:
    - bar (frame)
    - exit button
    - date and time
    - all open apps and their unminimize
    
    
    """
    def __init__(self,desktop):
        
        
        parent = Frame(desktop.desktop, bg="white")
        parent.pack(side='bottom')
        parent.pack_propagate(False)

        super().__init__(parent)
        
        self.parent=parent

        self.barFrame = Frame(master=desktop.desktop,bg="grey",height=50)

        self.exitButton = Button(master=self.barFrame,text="Exit",command=self.doExitButtonAction)

        self.unminimizeList = []


        self.barFrame.pack(side='bottom', fill="x",expand=False)
        
        self.exitButton.pack(side="left")
        

        
    def doExitButtonAction(self):
        self.parent.master.master.destroy()

    def addUnMini(self, button):
        self.unminimizeList.append(button)
        button.pack(side='left',padx=5)

    def removeUnMini(self,button):
        self.unminimizeList.remove(button)
        button.pack_forget()

        