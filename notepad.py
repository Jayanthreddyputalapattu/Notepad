from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


class Notepad: 
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("700x400")
    TextArea = Text(root,font=("airal",15))
    menubar = Menu(root)
    Filemenu = Menu(menubar,tearoff=0)
    Editmenu = Menu(menubar,tearoff=0)
    Helpemenu = Menu(menubar,tearoff=0)

    Scrollbar = Scrollbar(TextArea)
    file = None


    def __init__(self):
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)
        self.TextArea.grid(sticky=N+S+E+W)
        #file menu
        self.Filemenu.add_command(label="New",command=self.NewFile)
        self.Filemenu.add_command(label="Save",command=self.saveFile)
        self.Filemenu.add_command(label="Open",command=self.openFile)
        self.Filemenu.add_separator()
        self.Filemenu.add_command(label="Exit",activebackground="red",command=self.quitApplication)
        self.menubar.add_cascade(label="File",menu=self.Filemenu)

        #edit menu
        self.Editmenu.add_command(label="Select All                                          (ctrl+shift+a)",command=self.Select_all)
        self.Editmenu.add_command(label="cut                                          (ctrl+x)",command=self.cut)
        self.Editmenu.add_command(label="copy                                           (ctrl+c)",command=self.copy)
        self.Editmenu.add_command(label="Paste                                            (ctrl+v)",command=self.paste)
        self.menubar.add_cascade(label="Edit",menu=self.Editmenu)




        self.Helpemenu.add_command(label="About Notepad",command=self.showAbout)
        self.menubar.add_cascade(label="Help",menu=self.Helpemenu)

        self.root.config(menu=self.menubar)
        self.Scrollbar.pack(side=RIGHT,fill=Y)


        self.Scrollbar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.Scrollbar.set)


    def quitApplication(self):
        self.root.destroy()
    

    def openFile(self):
        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All files","*.*"),
                                    ("text document","*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file)+"- Notepad")
            self.TextArea.delete(1.0,END)
            file = open(self.file,"r")
            self.TextArea.insert(1.0,file.read())
            file.close()
    
    def NewFile(self):
        self.root.title("Untitled - Notepad")
        self.file =None
        self.TextArea.delete(1.0,END)

    def run(self):
        self.root.mainloop()
    

    def saveFile(self):
        if self.file == None:
            self.file = asksaveasfilename(initialfile="Untitled.txt",
                                          defaultextension=".txt",
                                          filetypes=[("All files","*.*"),
                                                     ("text document","*.txt")]
                                             )
            if self.file == "":
                self.file = None          
            else:
                file=open(self.file,"w")
                file.write(self.TextArea.get(1.0,END))
                file.close()


                

                self.root.title(os.path.basename(self.file)+" - Notepad")
        else:
            file = open(self.file,"w")
            file.write(self.TextArea.get(1.0,END))
            file.close()
    def cut(self):
        self.TextArea.event_generate("<<Cut>>")
    
    def paste(self):
        self.TextArea.event_generate("<<Paste>>")
    
    def Select_all(self):
        self.TextArea.event_generate("<<SelectAll>>")
    
    def copy(self):
        self.TextArea.event_generate("<<Copy>>")

    
    def showAbout(self):
        showinfo("Notepad","This is a notepad it can paste when we press ctrl+v,it can copy when we press ctrl+c and when we press ctrl+x it will cut and when we press ctrl+shift+a it will select all. and when you press file it will show four words if you press open it will open files select the which you and press ok and when press exit the notepad will exit and when we press Save it will open files agian and name file name and press ok when we press new it clear screen and when we press when we press Help then you will see about notepad and press it.it will show about notepad thats it.")

    
    
notepad = Notepad()
<<<<<<< HEAD
notepad.run()
=======
notepad.run()
>>>>>>> c1c1b2f6c97aaf6f571ba4160ac9f8d9026e32df
