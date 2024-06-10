from tkinter import *
from myFrameWindow  import myFrameWindow 
from myNotepadFrame  import myNotepadFrame
from myDesktopFrame import myDesktopFrame
from myFileManagerFrame import myFileManagerFrame
        

win =Tk()
win.attributes('-fullscreen', True)

desktop = myDesktopFrame(win)

exit_button = Button(desktop.desktop, text="Exit", command=win.destroy) 
exit_button.pack(anchor = "w",side="bottom") 

window2=myFrameWindow(myFileManagerFrame(desktop.desktop, (600,400)),"Example")

win.geometry("900x600")
win.title("Desktop")
win.mainloop()