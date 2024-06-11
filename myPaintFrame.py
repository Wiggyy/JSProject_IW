from tkinter import *
from tkinter import colorchooser,ttk

class myPaintFrame(Frame):

    def __init__(self,desktop,size):
        x,y = size
        
        parent = Frame(desktop, bg="white",width=x,height=y)
        parent.place(x=200,y=200)
        parent.pack_propagate(False)

        super().__init__(parent)
        self.parent=parent

        self.brushColor="Black"
        self.bgColor="White"
        self.startX =None
        self.startY=None
        self.penWidth = 5
        self.drawWidgets()
        self.canvas.bind('<B1-Motion>',self.paint)
        self.canvas.bind('<ButtonRelease-1>',self.reset)

        
    
    def paint(self, e):
        if(self.startX and self.startY):
            self.canvas.create_line(self.startX,self.startY,e.x,e.y,width=self.penWidth,fill=self.brushColor,capstyle='round',smooth=True)
        self.startX=e.x
        self.startY=e.y
    
    def reset(self, e):
        self.startX=None
        self.startY=None
    

    def changeWidth(self, width):
        self.penWidth = width
        
    def clearcanvas(self):
        self.canvas.delete(ALL)
        
    def changeBrushColor(self):
        self.brushColor = colorchooser.askcolor(color=self.brushColor)[1]
        self.colorButton.config(bg=self.brushColor)
        
    def drawWidgets(self):
        self.canvas = Canvas(self, width=500, height=400, bg=self.bgColor)
        self.controls = Frame(self, padx=5, pady=5)
        self.buttonFrame = Frame(master=self)
        self.buttonFrame.pack(side='top', fill="x",expand=False)
        self.controls.pack(side="left",fill="y")
        
        self.canvas.pack(side="right",fill="x", expand=False)
        
        self.loadButton = Button(master=self.buttonFrame,text="Load",command=self.doLoadButtonAction)
        self.saveButton = Button(master=self.buttonFrame,text="Save",command=self.doSaveButtonAction)
        self.clearButton = Button(master=self.buttonFrame,text="Clear",command=self.doClearButtonAction)
        self.colorButton = Button(master=self.controls,bg="Black",command=self.changeBrushColor,width=1,height=1)
        self.widthSlider = ttk.Scale(self.controls, from_=5, to=100, command=self.changeWidth, orient='vertical')
        self.widthSlider.set(self.penWidth)

        self.widthSlider.pack(side="left")
        self.colorButton.pack(side="left")
        self.loadButton.pack(side="left")
        self.saveButton.pack(side="left")
        self.clearButton.pack(side="left")
        
        
        self.popupFrame=None

    def doLoadButtonAction(self):

        self.showPopup(action='load')

    def doSaveButtonAction(self):
        self.showPopup(action='save')

    def doClearButtonAction(self):
        self.canvas.delete("all")

    
    def canvasToFile(self):
        all_lines = self.canvas.find_withtag("line") 
        allLineData =[""]
        for line_id in all_lines:
            print("deb1")
            x1, y1, x2, y2 = self.canvas.coords(line_id)
            line_color = self.canvas.itemcget(line_id, "fill")
            line_width = self.canvas.itemcget(line_id,"width")
            print(f"{x1},{y1},{x2},{y2},{line_color},{line_width}")
            allLineData.append(f"{x1},{y1},{x2},{y2},{line_color},{line_width}")
        print("deb")
        return allLineData
        
    
    def fileToCanvas(self,content):
        for line in content:
            if line.strip():
                x1, y1, x2, y2, savedFill, savedWidth = line.split(",")

                print(f"{x1},{y1},{x2},{y2},{savedFill},{savedWidth}")
                self.canvas.create_line(x1,y1,x2,y2,width=savedWidth,fill=savedFill,capstyle="round",smooth=True)
        


    
    def loadFromFile(self, file):
        try:
            with open(file, 'r') as f:
                content = f.readlines()
                self.canvas.delete("all")  
                self.fileToCanvas(content)
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error:", e)

    def saveToFile(self, file):
        try:
            with open(file, 'w') as f:
                self.canvas.addtag_all("line")
                for line_data in self.canvasToFile():
                    f.write(line_data + '\n')
            
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