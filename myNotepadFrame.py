from tkinter import *

class myNotepadFrame(Frame):
    """
    This is one of the "contents" for myFrameWindow
    It consists of:
    - button frame 
    - place to write in - scrollable
    - buttons on top (Save,Rename,Clear,Format*)
    
    
    """
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent
        self.buttonFrame = Frame(master=self)
        self.loadButton = Button(master=self.buttonFrame,text="Load",command=self.doLoadButtonAction)
        self.saveButton = Button(master=self.buttonFrame,text="Save",command=self.doSaveButtonAction)
        self.clearButton = Button(master=self.buttonFrame,text="Clear",command=self.doClearButtonAction)
        self.renameButton =  Button(master=self.buttonFrame,text="Rename",command=self.doRenameButtonAction)
        self.formatButton =  Button(master=self.buttonFrame,text="Format",command=self.doFormatButtonAction)
        self.mainText = Text(master=self)
        self.mainTxtScroll = Scrollbar(master=self.mainText,command=self.mainText.yview)
        self.mainText['yscrollcommand'] = self.mainTxtScroll.set


        self.buttonFrame.pack(side='top', fill="x",expand=False)
        self.mainText.pack(side='bottom',fill="both",expand=True)
        self.mainTxtScroll.pack(side='right',fill=Y)
        self.loadButton.pack(side="left")
        self.saveButton.pack(side="left")
        self.renameButton.pack(side="left")
        self.formatButton.pack(side="left")
        self.clearButton.pack(side="left")

        
    def doLoadButtonAction(self):
        print("Loading")

    def doSaveButtonAction(self):
        print("Saving")

    def doClearButtonAction(self):
        print("Clearing")

    def doRenameButtonAction(self):
        print("Renaming")

    def doFormatButtonAction(self):
        print("Formatting")
        