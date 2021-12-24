from tkinter import *
import smtplib, ssl


smtp_server = "smtp.gmail.com"
port = 465

sender = "igaro54teamfox@gmail.com"
password = "Google56"

context = ssl.create_default_context()

global server

class main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.widgets()

    def widgets(self):
        Label(self, text="Pour envoyer un mail, veuillez renseigner les informations ci-dessous\n").pack()
        Label(self, text="A :").pack()

        self.to_entry = Entry(self)
        self.to_entry.pack()

        Label(self, text="Objet :").pack()

        self.object_entry = Entry(self)
        self.object_entry.pack()

        Label(self, text="Message :").pack()

        self.msg_entry = Entry(self)
        self.msg_entry.pack()

        send_button = Button(self, text="Envoyer", command=self.send_mail)
        send_button.pack()

        quit_button = Button(self, text="Quitter", command=self.quit)
        quit_button.pack()

    def send_mail(self):
        message = """
From: {}
To: {}
Subject: {}

{}""".format(sender, self.to_entry.get(), self.object_entry.get(), self.msg_entry.get())
        server.sendmail(sender, self.to_entry.get(), message)


with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #Connecting to my mail account
    server.login(sender, password)
    main().mainloop()