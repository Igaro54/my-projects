from tkinter import *
from functools import partial

class calculator(Tk):
    
    def __init__(self):
        
        Tk.__init__(self)
        
        self.numbers = []
        self.result = 0

        self.widgets()
    
    def widgets(self):
        
        number_col = 3  #Default values used for positioning numbers on grid
        number_row = 2
        
        operator_row = 2

        operators = ["+", "*", "-", "/"]

        Label(self, text="Calculatrice").grid(column=0, row=0, columnspan=5)
        
        self.input_text = Label(self, text= "                 ", background="grey")
        self.input_text.grid(column=0, row=1, columnspan=5)

        for i in range(9,0,-1):
            if number_col > 0:
                Button(self, text=i, command=partial(self.append_input, i)).grid(column=number_col, row=number_row)
                number_col -= 1
                if number_col == 0:
                    number_col = 3
                    number_row += 1

        for item in operators:
            Button(self, text=item, command=partial(self.calculate, item)).grid(column=4, row=operator_row)
            operator_row += 1

        result_button = Button(self, text="Valider", command=self.validate)
        result_button.grid(column=0, row=6, columnspan=5)

    def append_input(self, button):
        
        input_list = list(self.input_text["text"])
        input_list.pop(0)
        input_list.append(str(button))
        
        self.input_text["text"] = "".join(input_list)
        
    def calculate(self, operator):
        
        actual_operator = operator
        
        a = 0
        
        for char in self.input_text["text"]:
            try:
                int(char)
            except ValueError:
                a += 1
        
        if a != len(self.input_text["text"]):
            
            self.numbers.append(self.input_text["text"].replace(" ", ""))
            self.input_text["text"] = "                 "
            
            if len(self.numbers) == 2:
                
                if actual_operator == "+":
                    for nbr in self.numbers:
                        self.result += int(nbr)
    
                if actual_operator == "-":
                    for nbr in self.numbers:
                        self.result = self.result - int(nbr)

    def validate(self):
        
        self.input_text["text"] = str(self.result)

calculator().mainloop()