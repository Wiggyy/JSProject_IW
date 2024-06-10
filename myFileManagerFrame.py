from tkinter import *
from os import *

class myFileManagerFrame(Frame):
    """
    This is one of the "contents" for myFrameWindow
    It consists of:
    - location - textfield
    - list of objects (folders/files)
    - topbuttons
    
    """
    def __init__(self,desktop,size):
        x,y = size
        
        parent = Frame(desktop, bg="white",width=x,height=y)
        parent.place(x=200,y=200)
        parent.pack_propagate(False)

        super().__init__(parent)
        
        self.buttonFrame = Frame(master=self,background="Light grey",height=25)
        self.locationFrame = Frame(master=self,background="Light grey",height=25)
        self.openButton = Button(master=self.buttonFrame,text="Open",command=self.doOpenButtonAction)
        self.deleteButton = Button(master=self.buttonFrame,text="Save",command=self.doDeleteButtonAction)
        self.renameButton =  Button(master=self.buttonFrame,text="Rename",command=self.doRenameButtonAction)
        self.addFolderButton =  Button(master=self.buttonFrame,text="Add Folder",command=self.doAddFolderButtonAction)
        self.locationLabel = Label(master=self.locationFrame,text="Location: ",background="Light grey")
        self.locationBox = Text(master=self.locationFrame,padx=20, width=50)

        self.mainListBox = Listbox(master=self)
        self.mainTxtScroll = Scrollbar(master=self.mainListBox,command=self.mainListBox.yview)
        self.mainListBox['yscrollcommand'] = self.mainTxtScroll.set


        self.buttonFrame.pack(side='top', fill="x",expand=False)
        self.locationFrame.pack(side='top', fill="x",expand=False)
        self.locationFrame.pack_propagate(False)
        self.buttonFrame.pack_propagate(False)
        self.mainListBox.pack(side='bottom',fill="both",expand=True)
        self.mainTxtScroll.pack(side='right',fill=Y)
        self.openButton.pack(side="left")
        self.deleteButton.pack(side="left")
        self.renameButton.pack(side="left")
        self.addFolderButton.pack(side="left")
        self.locationLabel.pack(side="left",padx=10)
        self.locationBox.pack(side='left',padx=10)


        
    def doDeleteButtonAction(self):
        print("Deleting")

    def doOpenButtonAction(self):
        print("Opening")

    def doRenameButtonAction(self):
        print("Renaming")

    def doAddFolderButtonAction(self):
        print("Adding Folder")

    def pupulate(self):
        pass


        