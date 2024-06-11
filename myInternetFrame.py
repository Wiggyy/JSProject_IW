from tkinter import *
from tkinter import font
class myInternetFrame(Frame):
    """
    This is one of the "contents" for myFrameWindow
    It consists of:
    - button frame 
    - place to write in - scrollable
    - buttons on top (Save,Rename,Clear,Format*)
    
    
    """
    def __init__(self,desktop,size):
        x,y = size
        
        parent = Frame(desktop, bg="white",width=x,height=y)
        parent.place(x=200,y=200)
        parent.pack_propagate(False)

        super().__init__(parent)
        self.parent=parent
        self.drawWidgets()


        
    
    def drawWidgets(self):
        font1 = font.Font(family="Arial", size=20, weight="bold")
        font2 = font.Font(family="Arial", size=12)
        font3 = font.Font(family="Arial", size=12, weight="bold")


        self.mainFrame = Frame(master=self,bg="White")
        
        self.gameFrame = Frame(master=self.mainFrame, bg="red",width=250,height=150)

        self.urlFrame = Frame(master=self.mainFrame,background="Light grey",height=25)
        self.urlLabel = Label(master=self.urlFrame,text="URL: ",background="Light grey")
        self.urlBox = Entry(master=self.urlFrame, width=50)
        self.urlBox.insert(0, "https://oggole.com")
        self.urlBox.config(state=DISABLED)

        self.mainLabel1 = Label(master=self.mainFrame,text="No internet",font=font1,bg="White")
        self.mainLabel2 = Label(master=self.mainFrame,text="Try:",font=font2,bg="White")
        self.mainLabel3 = Label(master=self.mainFrame, text="- Checking the network cables,modem, and router", font=font2,bg="White")
        self.mainLabel4 = Label(master=self.mainFrame, text="- Reconnecting to Wi-Fi", font=font2,bg="White")
        self.mainLabel5 = Label(master=self.mainFrame, text="ERR_INTERNET_DISCONNECTED", font=font3,bg="White")

        self.mainFrame.pack(fill="both")
        self.urlFrame.pack(side="top", fill="x",expand=False)
        self.urlFrame.pack_propagate(False)
        self.urlLabel.pack(side='left',padx=10)
        self.urlBox.pack(side="left",padx=10)
        self.urlBox.pack_propagate(False)
        self.gameFrame.pack(side="top",padx=15)
        self.mainLabel1.pack(pady=(20, 10))
        self.mainLabel2.pack(anchor="w", padx=80)
        self.mainLabel3.pack(anchor="w", padx=100)
        self.mainLabel4.pack(anchor="w", padx=100)
        self.mainLabel5.pack(pady=(20, 10))
        
        
        
        
    
        