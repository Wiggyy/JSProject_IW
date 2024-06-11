from tkinter import *
from os import *
from os import listdir, mkdir, rename, remove
from os.path import isdir, join, exists, abspath
import shutil

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
        self.deleteButton = Button(master=self.buttonFrame,text="Delete",command=self.doDeleteButtonAction)
        self.renameButton =  Button(master=self.buttonFrame,text="Rename",command=self.doRenameButtonAction)
        self.addFolderButton =  Button(master=self.buttonFrame,text="Add Folder",command=self.doAddFolderButtonAction)
        self.locationLabel = Label(master=self.locationFrame,text="Location: ",background="Light grey")
        self.locationBox = Text(master=self.locationFrame,padx=20, width=50)
        self.goLocationButton =  Button(master=self.locationFrame,text="Go",command=self.doGoLocationButtonAction)

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
        self.goLocationButton.pack(side='left',padx=10)

        self.current_path = "folderManager"
        if not exists(self.current_path):
            mkdir(self.current_path)

        self.locationBox.insert(END, self.current_path)
        self.popupFrame = None
        self.confirmationPopupFrame = None
        self.populate()




        
    def doDeleteButtonAction(self):
        selected = self.mainListBox.curselection()
        if not selected:
            print("No item selected to delete.")
            return
        item = self.mainListBox.get(selected[0])
        self.showDeleteConfirmationPopup(item)

    def showDeleteConfirmationPopup(self, item):
        if self.confirmationPopupFrame:  # Destroy any existing confirmation popup frame
            self.confirmationPopupFrame.destroy()
        
        self.confirmationPopupFrame = Frame(self, bg="lightgrey", padx=10, pady=10)
        self.confirmationPopupFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label = Label(self.confirmationPopupFrame, text=f"Are you sure that you want to delete {item} and everything in it?")
        label.pack(side=TOP, padx=5, pady=5)

        def confirm():
            path = join(self.current_path, item)
            try:
                if isdir(path):
                    shutil.rmtree(path)
                else:
                    remove(path)
                self.populate()
                print(f"Deleted {item}")
            except Exception as e:
                print(f"Failed to delete {item}: {e}")
            self.confirmationPopupFrame.destroy()
            self.confirmationPopupFrame = None

        def cancel():
            self.confirmationPopupFrame.destroy()
            self.confirmationPopupFrame = None

        confirm_button = Button(self.confirmationPopupFrame, text="Confirm", command=confirm)
        confirm_button.pack(side=LEFT, padx=5, pady=5)

        cancel_button = Button(self.confirmationPopupFrame, text="Cancel", command=cancel)
        cancel_button.pack(side=LEFT, padx=5, pady=5)
        
    def doOpenButtonAction(self):
        selected = self.mainListBox.curselection()
        if not selected:
            print("No item selected to open.")
            return
        item = self.mainListBox.get(selected[0])
        path = join(self.current_path, item)
        if isdir(path):
            self.current_path = path
            self.locationBox.delete(1.0, END)
            self.locationBox.insert(END, self.current_path)
            self.populate()
            print(f"Opened directory {item}")
        else:
            print(f"Cannot open file {item}")

    def doRenameButtonAction(self):
        selected = self.mainListBox.curselection()
        if not selected:
            print("No item selected to rename.")
            return
        item = self.mainListBox.get(selected[0])
        self.showPopup(item, action='rename')

    def doAddFolderButtonAction(self):
        self.showPopup(action='create')

    def showPopup(self, item=None, action='create'):
        if self.popupFrame:  # Destroy any existing popup frame
            self.popupFrame.destroy()
        
        self.popupFrame = Frame(self, bg="lightgrey", padx=10, pady=10)
        self.popupFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label = Label(self.popupFrame, text="New Name:")
        label.pack(side=LEFT, padx=5, pady=5)

        new_name_entry = Entry(self.popupFrame)
        new_name_entry.pack(side=LEFT, padx=5, pady=5)

        def confirm():
            new_name = new_name_entry.get().strip()
            if not new_name:
                print("No name provided.")
                return
            if action == 'create':
                new_folder_path = join(self.current_path, new_name)
                if exists(new_folder_path):
                    print("Folder already exists.")
                    return
                try:
                    mkdir(new_folder_path)
                    self.populate()
                    print(f"Added folder {new_name}")
                except Exception as e:
                    print(f"Failed to add folder {new_name}: {e}")
            elif action == 'rename':
                old_path = join(self.current_path, item)
                new_path = join(self.current_path, new_name)
                try:
                    rename(old_path, new_path)
                    self.populate()
                    print(f"Renamed {item} to {new_name}")
                except Exception as e:
                    print(f"Failed to rename {item}: {e}")
            self.popupFrame.destroy()
            self.popupFrame = None

        def cancel():
            self.popupFrame.destroy()
            self.popupFrame = None

        confirm_button = Button(self.popupFrame, text="Create" if action == 'create' else "Rename", command=confirm)
        confirm_button.pack(side=LEFT, padx=5, pady=5)

        cancel_button = Button(self.popupFrame, text="Cancel", command=cancel)
        cancel_button.pack(side=LEFT, padx=5, pady=5)

    def populate(self):
        try:
            self.mainListBox.delete(0, END)
            items = listdir(self.current_path)
            for item in items:
                self.mainListBox.insert(END, item)
            print("List populated.")
            self.locationBox.delete(1.0, END)
            self.locationBox.insert(END, self.current_path)
        except Exception as e:
            print(f"Failed to populate list: {e}")

    def doGoLocationButtonAction(self):
        new_path = self.locationBox.get(1.0, END).strip()
        if not exists(new_path):
            print(f"Path does not exist: {new_path}")
            return
        self.current_path = new_path
        self.populate()
        print(f"Changed current path to {self.current_path}")

   



        