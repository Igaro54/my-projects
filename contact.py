from tkinter import Tk, Label, Entry, Button, Toplevel, messagebox
from functools import partial

class main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Créer un nouveau contact")
        self.geometry("400x300")
        self.contact_list = {}
        self.widgets()
    
    def widgets(self):
        Label(self, text="Entrer le nom du contact").pack()
        self.name_entry = Entry(self)
        self.name_entry.pack()
        Label(self, text="Entrer l'adresse du contact").pack()
        self.adress_entry = Entry(self)
        self.adress_entry.pack()
        Label(self, text="Entrer le numéro associé au contact").pack()
        self.phone_entry = Entry(self)
        self.phone_entry.pack()
        Label(self, text="Entrer l'adresse-mail associé au contact").pack()
        self.mail_entry = Entry(self)
        self.mail_entry.pack()
        Button(self, text="Valider", command=self.validate).pack()
        Button(self, text="Voir les contacts enregistrés", command=self.show_contacts).pack()
        Button(self, text="Quitter", command=self.quit).pack()
    
    def validate(self):
        if self.name_entry.get() != "":
            self.contact_list.update({self.name_entry.get():[self.adress_entry.get(), self.phone_entry.get(), self.mail_entry.get()]})
        else:
            Label(self, text="Veuillez ajouter un nom à votre contact").pack()

    def show_contacts(self):
        if len(self.contact_list) > 0:
            self.contact_window = Toplevel(self)
            self.contact_window.title("Liste des contacts enregistrés")
            for key in self.contact_list:
                self.contact = Button(self.contact_window, text=f"{key}")
                self.contact.configure(command=lambda name=self.contact.cget("text"):self.show_contacts_details(name))
                self.contact.pack()
            Button(self.contact_window, text="Quitter", command=self.contact_window.destroy).pack()
        else:
            error = Label(self, text="Vous n'avez pas encore de contact enregistré")
            error.pack()
    
    def show_contacts_details(self, name):
        self.details_window = Toplevel(self.contact_window)
        self.details_window.title("Détails du contact")
        for key in self.contact_list:
            if key == name:
                if self.contact_list[key][0] == "" and self.contact_list[key][1] == "" and self.contact_list[key][2] == "":
                    Label(self.details_window, text="Ce contact n'a aucune information attribuée").pack()
                    break
                if self.contact_list[key][0] != "":
                    Label(self.details_window, text=f"Adresse : {self.contact_list[key][0]}").pack()
                if self.contact_list[key][1] != "":
                    Label(self.details_window, text=f"Téléphone : {self.contact_list[key][1]}").pack()
                if self.contact_list[key][2] != "":
                    Label(self.details_window, text=f"Adresse-mail : {self.contact_list[key][2]}").pack()
        Button(self.details_window, text="Retirer ce contact", command=partial(self.remove_contact, name)).pack()
        Button(self.details_window, text="Quitter", command=self.details_window.destroy).pack()

    def remove_contact(self, name):
        remove = messagebox.askyesno("Supprimer un contact", "Êtes-vous sûr de vouloir supprimer ce contact ?")
        if remove == True:
            for key in self.contact_list:
                if key == name:
                    del self.contact_list[key]
                    break
            self.contact_window.destroy()

main().mainloop()