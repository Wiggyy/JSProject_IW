from tkinter import *


class topBar(Frame):
    def __init__(self,parent,label):
       

        self.parent=parent
        
        self.topbar = Frame(master=self.parent, bg="PaleTurquoise",height=20)
        self.topbar.pack(side="top",fill="x")
        self.topbar.bind("<B1-Motion>",self.on_drag)
        self.topbar.bind("<ButtonRelease>",self.on_drop)
        self.topbar.bind("<Button-1>", self.start_drag)
        self.topbar.pack_propagate(False)

        self.title=Label(master=self.topbar,text=label,bg=self.topbar['bg'])
        self.title.pack(side="left")
        self.title.bind("<B1-Motion>",self.on_drag)
        self.title.bind("<ButtonRelease>",self.on_drop)
        self.title.bind("<Button-1>", self.start_drag)

        self.closeButton= Button(master=self.topbar, text="X",command=self.close,width=2,)
        self.closeButton.pack(side="right",fill="y")

        self.minButton= Button(master=self.topbar, text="-",command=self.minimize,width=2,)
        self.minButton.pack(side="right",fill="y")

        self.startX=0
        self.startY=0

    def start_drag(self, event):
        self.startX = event.x_root - self.parent.winfo_x()
        self.startY = event.y_root - self.parent.winfo_y()
        self.parent.lift()

    def on_drag(self, event):
        x = self.parent.winfo_pointerx() - self.startX
        y = self.parent.winfo_pointery() - self.startY
        self.parent.place(x=x, y=y)
        self.parent.lift()

    def on_drop(self, event):
        x = self.parent.winfo_pointerx() - self.startX
        y = self.parent.winfo_pointery() - self.startY
        self.parent.place(x=x, y=y)

        self.startX = self.parent.winfo_pointerx() - self.startX
        self.startY = self.parent.winfo_pointery() - self.startY
        self.parent.lift()

    def close(self):
        self.parent.place_forget()
        self.parent.destroy()

    def minimize(self):
        
        self.parent.place_forget()

    def unminimize(self):
        self.parent.place(x=self.startX, y=self.startY)
        self.parent.lift()

class myFrameWindow():
    def __init__(self, content,label) -> None:
        
        self.parent = content.master

        self.topbar= topBar(self.parent,label=label)

        self.content = content
        self.content.pack(side="bottom",fill="both",expand="true")

        self.unminiButt=Button(master=self.parent.master, text="-",command=self.topbar.unminimize,width=2,)
        self.unminiButt.pack(side="right",fill="y")
        

        
     