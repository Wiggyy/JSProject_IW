from tkinter import *
from myFrameWindow  import myFrameWindow 
from myNotepadFrame  import myNotepadFrame
from myDesktopFrame import myDesktopFrame
from myFileManagerFrame import myFileManagerFrame
from myToolBarFrame import myToolBarFrame

win =Tk()
win.attributes('-fullscreen', True)

openApps=[]
desktop = myDesktopFrame(win,openApps)
toolBar = myToolBarFrame(desktop)
desktop.addToolBar(toolBar)

#window2=myFrameWindow(myFileManagerFrame(desktop.desktop, (600,400)),"Example",toolBar,"")

win.geometry("900x600")
win.title("Desktop")
win.mainloop()