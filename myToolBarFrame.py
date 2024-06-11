from tkinter import *
from datetime import datetime

class myToolBarFrame(Frame):

    def __init__(self,desktop):
        
        
        parent = Frame(desktop.desktop, bg="white")
        parent.pack(side='bottom')
        parent.pack_propagate(False)

        super().__init__(parent)

        self.parent=parent

        self.drawWidgets()

        self.unminimizeList = []
        
       
        self.updateTime()

        
    def doExitButtonAction(self):
        self.parent.master.master.destroy()

    def addUnMini(self, button):
        self.unminimizeList.append(button)
        button.pack(side='left',padx=5)

    def removeUnMini(self,button):
        self.unminimizeList.remove(button)
        button.pack_forget()

    def updateTime(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.timeLabel.config(text=current_time)
        self.timeLabel.after(1000, self.updateTime)

    def drawWidgets(self):
        self.barFrame = Frame(master=self.parent.master,bg="grey",height=50)

        self.exitButton = Button(master=self.barFrame,text="Exit",command=self.doExitButtonAction)
        self.timeLabel = Label(master=self.barFrame,text=datetime.now(),bg="grey")

        self.barFrame.pack(side='bottom', fill="x",expand=False)
        
        self.exitButton.pack(side="left")
        self.timeLabel.pack(side="right")

        