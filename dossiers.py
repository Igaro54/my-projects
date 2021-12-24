from tkinter import *
from tkinter import filedialog
import os

class main(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.widgets()
    
    def widgets(self):
        self.button = Button(self, text="Parcourir les dossiers", command=self.folderManagemennt).pack()
    
    def folderManagemennt(self):
        folderDir = filedialog.askdirectory()
        for i in os.listdir(folderDir):
            Label(self, text=i.split(".")[0]).pack()
            
main().mainloop()