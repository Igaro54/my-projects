from tkinter import *
from functools import partial

class identifier(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Se connecter")
        self.config(background="#c7464e")
        
        self.widgets()
        self.bind('<Return>', self.validate)
    
    def widgets(self):
        username_text = Label(self, text="Nom d'utilisateur", background=self["background"])
        username_text.grid(column=0, row=0) 
        
        self.username_entry = Entry(self)
        self.username_entry.grid(column=1, row=0)
        
        password_text = Label(self, text="Mot de passe", background=self["background"])
        password_text.grid(column=0, row=1)
        
        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(column=1, row=1)
        
        self.valid_button = Button(self, text="Valider", command=partial(self.validate, None))
        self.valid_button.grid(column=0, row=2)
        self.valid_button.propagate(0)
        
        quit_button = Button(self, text="Quitter", command=self.quit)
        quit_button.grid(column=1, row=2)
        quit_button.propagate(0)

    def validate(self, event):
        if self.username_entry.get() == "Igaro" and self.password_entry.get() == "8426":
            self.destroy()
            main()
        else:
            if self.valid_button["state"] != DISABLED:
                self.valid_button.config(state=DISABLED)
                
                error_text = Label(self, text="Nom d'utilisateur ou mot de passe invalide")
                error_text.grid(column=1, row=3)
                
                self.after(3000, self.quit)
                
class main(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("K Project")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        
        self.fullscreen = True
        self.bind("<F11>", self.toogleFullscreen)

        self.geometry("{}x{}".format(self.screen_width, self.screen_height))
        self.config(background="#c7464e")
        
        self.widgets()
    
    def widgets(self):

        title = Label(text="Bienvenue Igaro", background=self["background"])
        title.config(font=("MS PGothic", 70))
        title.place(relx=0.5, rely=0.02, anchor=N)

        button_frame = Frame(self, padx=self.screen_width, background=self["background"], highlightthickness=2, highlightbackground="black")
        button_frame.place(relx=0.5, rely=0.15, anchor=N)

        app_button = Button(button_frame, text="Appli", command=self.app_clicked, background=self["background"], relief=FLAT, activebackground=self["background"], cursor="hand2")
        app_button.config(font=("Arial Black", 15))
        app_button.grid(column=1, row=0, padx=self.screen_width/10, ipadx=50, ipady=20,sticky=NSEW)
        
        file_button = Button(button_frame, text="Fichier", command=None, background=self["background"], relief=FLAT, activebackground=self["background"], cursor="hand2")
        file_button.config(font=("Arial Black", 15))
        file_button.grid(column=2, row=0, padx=self.screen_width/10, ipadx=50, ipady=20, sticky=NSEW)

        music_button = Button(button_frame, text="Musique", command=None, background=self["background"], relief=FLAT, activebackground=self["background"], cursor="hand2")
        music_button.config(font=("Arial Black", 15))
        music_button.grid(column=3, row=0, padx=self.screen_width/10, ipadx=50, ipady=20, sticky=NSEW)
        
        self.elem_frame = Frame(self, padx=self.screen_width-1340, pady=350, background=self["background"], highlightthickness=2, highlightbackground="black")
        self.elem_frame.pack(side=BOTTOM)

        self.elem_text = Label(self.elem_frame, text="Choisissez un menu pour commencer à naviguer", background=self["background"])
        self.elem_text.config(font=("Arial", 25))
        self.elem_text.grid(column=0, row=0)
    
    def toogleFullscreen(self, event):
        if self.fullscreen == True:
            self.attributes("-fullscreen", True)
            self.fullscreen = False
        else:
            self.attributes("-fullscreen", False)
            self.fullscreen = True

    def app_clicked(self):
        adding_button = Button(self.elem_text, text="Ajouter un raccourci", command=None, background=self["background"], relief=FLAT, activebackground=self["background"], cursor="hand2")
        adding_button.pack()

identifier().mainloop()