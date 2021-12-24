from tkinter import *

class main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Démineur")
        self.widgets()

    def widgets(self):
        for i in range(0,9):
            for j in range(0,9):
                self.mines = Button(self, text="", command=self.test).grid(row=i, column=j, ipadx=10, ipady=4)
    
    def test(self):
        self.mines.config(state=DISABLED)

main().mainloop()