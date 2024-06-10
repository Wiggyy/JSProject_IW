from tkinter import *
from myFrameWindow  import myFrameWindow 
from myNotepadFrame  import myNotepadFrame
    
        
"""def makeButt(myFrameList,count,contentList,mainFrameList):
    count[0]+=1
    mainFrameList.append(Frame(desktop, bg="white",width=200,height=200))
    mainFrameList[count[0]-1].place(x=0,y=0)
    mainFrameList[count[0]-1].pack_propagate(False)
    #contentList.append(Frame(master=mainFrameList[count[0]-1],bg="white"))
    contentList.append(myNotepadFrame(mainFrameList[count[0]-1]))
    myFrameList.append(myFrameWindow(contentList[count[0]-1],f"Example{count}"))
    print(count[0])
    print(len(myFrameList))"""


win =Tk()
desktop = Frame(win,bg="gray")
desktop.pack(fill="both", expand=True)

f1 = Frame(desktop, bg="white",width=200,height=200)
#f2 = Frame(desktop, bg="white",width=200,height=200)
f1.place(x=0,y=0)
f1.pack_propagate(False)
#f2.place(x=0,y=0)
#f2.pack_propagate(False)

f1_2 = Frame(f1, bg="white")

#f1_3 = Frame(f2, bg="lightGray")

"""count=[0]
listtt=[]
conList=[]
mainList=[]
AddWindowButt=Button(master=desktop,text=f"Add Window{count}",width=50,height=25,command=lambda:makeButt(listtt,count,conList,mainList))
AddWindowButt.pack(side="left")"""

window2=myFrameWindow(myNotepadFrame(f1),"Example")
#window3=myFrameWindow(f1_3,"Example 2")


win.geometry("900x600")
win.title("desktop test")
win.mainloop()