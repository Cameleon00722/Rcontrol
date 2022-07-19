from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
import json

window = Tk()


def etat(Cocher):
    Cocher = False

    for i in C1.state():
        if i == "selected":
            print("c1 cocher")
            Cocher = True

    for i in C2.state():
        if i == "selected":
            print("c2 cocher")
            Cocher = True
            print(Cocher)

    for i in C3.state():
        if i == "selected":
            print("c3 cocher")
            Cocher = True

    for i in C4.state():
        if i == "selected":
            print("c4 cocher")
            Cocher = True
    return Cocher


def getEntry():
    Cocher = False
    Err = False
    Capi = txtfld.get()

    titre1 = txtfld1.get()

    Img = txtfld2.get()

    if len(Capi) == 0:
        messagebox.showinfo("Erreur", "merci de remplir la clé api")
        Err = True
    elif not etat(Cocher):
        messagebox.showinfo("Erreur", "merci de cocher au moins 1 case")
        Err = True
    elif len(titre1) == 0:
        messagebox.showinfo("Erreur", "merci de donner un titre")
        Err = True
    elif not Err:

        lst2 = []

        for i in C1.state():
            if i == "selected":
                lst2.append("twitter")

        for i in C2.state():
            if i == "selected":
                lst2.append("tiktok")

        for i in C3.state():
            if i == "selected":
                lst2.append("instagram")

        for i in C4.state():
            if i == "selected":
                lst2.append("linkedin")

        payload = {
            "post": titre1,
            "platforms": lst2,
            "mediaUrls": [Img]
        }

        Capi = "Bearer " + txtfld.get()
        # Live API Key
        headers = {'Content-Type': 'application/json',
                   'Authorization': Capi}

        r = requests.post('https://app.ayrshare.com/api/post',
                          json=payload,
                          headers=headers)
        messagebox.showinfo("Retour json", r.json())


def analyse():
    lst = []

    for i in C1.state():
        if i == "selected":
            print("c1 cocher")
            lst.append("twitter")

    for i in C2.state():
        if i == "selected":
            print("c2 cocher")
            lst.append("tiktok")

    for i in C3.state():
        if i == "selected":
            print("c3 cocher")
            lst.append("instagram")

    for i in C4.state():
        if i == "selected":
            print("c4 cocher")
            lst.append("linkedin")

    Capi = "Bearer " + txtfld.get()
    print(Capi)

    payload = {'platforms': lst}
    headers = {'Content-Type': 'application/json',
               'Authorization': Capi}

    r = requests.post('https://app.ayrshare.com/api/analytics/social',
                      json=payload,
                      headers=headers)

    messagebox.showinfo("Retour json", r.json())


txtfld = Entry(window, text="clé api", bd=5)
txtfld.place(x=340, y=50)
lbl2 = Label(window, text="clé api", fg='red', font=("Helvetica", 16))
lbl2.place(x=260, y=47)

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()

C1 = ttk.Checkbutton(window, text="twitter", variable=v1, onvalue=1, offvalue=0)
C1.grid(column=0, row=0)

C2 = ttk.Checkbutton(window, text="Tiktok", variable=v2)
C2.grid(column=0, row=0)

C3 = ttk.Checkbutton(window, text="Instagram", variable=v3)
C3.grid(column=0, row=0)

C4 = ttk.Checkbutton(window, text="Linkedin", variable=v4)
C4.grid(column=0, row=0)

C1.place(x=300, y=100)
C2.place(x=470, y=100)
C3.place(x=300, y=150)
C4.place(x=470, y=150)

lbl = Label(window, text="titre", fg='red', font=("Helvetica", 16))
lbl.place(x=250, y=260)
txtfld1 = Entry(window, text="titre", bd=5)
txtfld1.place(x=250, y=300)

lbl1 = Label(window, text="media url", fg='red', font=("Helvetica", 16))
lbl1.place(x=460, y=260)
txtfld2 = Entry(window, text="image", bd=5)
txtfld2.place(x=460, y=300)

btn = Button(window, text="envoyer", fg='blue', command=getEntry)
btn.place(x=700, y=450)

btn = Button(window, text="analyser", fg='blue', command=analyse)
btn.place(x=100, y=450)

# loop maj de la page

window.title('Rcontrol')
window.iconbitmap('logo.ico')
window.geometry("800x500+10+20")
window.mainloop()
