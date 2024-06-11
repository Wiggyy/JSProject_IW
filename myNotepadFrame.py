from tkinter import *


class myNotepadFrame(Frame):
  
    def __init__(self,desktop,size,file=None):
        x,y = size
        
        parent = Frame(desktop, bg="white",width=x,height=y)
        parent.place(x=200,y=200)
        parent.pack_propagate(False)

        super().__init__(parent)
        
        self.drawWidgets()
        if file:
            self.loadFromFile(file)

        self.popupFrame=None


        
    def doLoadButtonAction(self):

        self.showPopup(action='load')

    def doSaveButtonAction(self):
        self.showPopup(action='save')

    def doClearButtonAction(self):
        self.mainText.delete('1.0', 'end')


    def loadFromFile(self, file):
        try:
            with open(file, 'r') as f:
                content = f.read()
                self.mainText.delete('1.0', 'end') 
                self.mainText.insert('1.0', content)  
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error:", e)

    def saveToFile(self, file):
        try:
            with open(file, 'w') as f:

                f.write(self.mainText.get('1.0', 'end'))
            
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error:", e)

    def showPopup(self, item=None, action='load'):
        if self.popupFrame: 
            self.popupFrame.destroy()
        
        self.popupFrame = Frame(self, bg="lightgrey", padx=10, pady=10)
        self.popupFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label = Label(self.popupFrame, text="Path:")
        label.pack(side=LEFT, padx=5, pady=5)

        pathEntry = Entry(self.popupFrame)
        pathEntry.pack(side=LEFT, padx=5, pady=5)

        def confirm():
            path = pathEntry.get().strip()
            if not path:
                print("No name provided.")
                return
            if action == 'load':
                self.loadFromFile(path)
            elif action == 'save':
                self.saveToFile(path)
            self.popupFrame.destroy()
            self.popupFrame = None

        def cancel():
            self.popupFrame.destroy()
            self.popupFrame = None

        confirm_button = Button(self.popupFrame, text="Load" if action == 'load' else "Save", command=confirm)
        confirm_button.pack(side=LEFT, padx=5, pady=5)

        cancel_button = Button(self.popupFrame, text="Cancel", command=cancel)
        cancel_button.pack(side=LEFT, padx=5, pady=5)
    def drawWidgets(self):
        self.buttonFrame = Frame(master=self)
        self.loadButton = Button(master=self.buttonFrame,text="Load",command=self.doLoadButtonAction)
        self.saveButton = Button(master=self.buttonFrame,text="Save",command=self.doSaveButtonAction)
        self.clearButton = Button(master=self.buttonFrame,text="Clear",command=self.doClearButtonAction)
        self.mainText = Text(master=self)
        self.mainTxtScroll = Scrollbar(master=self.mainText,command=self.mainText.yview)
        self.mainText['yscrollcommand'] = self.mainTxtScroll.set


        self.buttonFrame.pack(side='top', fill="x",expand=False)
        self.mainText.pack(side='bottom',fill="both",expand=True)
        self.mainTxtScroll.pack(side='right',fill=Y)
        self.loadButton.pack(side="left")
        self.saveButton.pack(side="left")

        self.clearButton.pack(side="left")


        