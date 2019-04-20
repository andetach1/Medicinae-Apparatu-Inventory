#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import ttk, font
import getpass
class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        gui_style = ttk.Style()
        gui_style.configure('My.TFrame', background='#F4E8F4')
        can= Canvas(self.raiz)
        can.pack(fill=BOTH)


        self.raiz.geometry("500x400")
        self.raiz.resizable(1,1)
        self.raiz.title("MAI")
        self.fuente = font.Font(weight='bold')
        self.etiq1 = Label(self.raiz,bg="#F4E8F4",fg="purple", text="User:",font=self.fuente)
        self.etiq2 = Label(self.raiz,bg="#F4E8F4", fg="purple",text="Password:",font=self.fuente)
        self.mensa = StringVar()
        self.etiq3 = Label(self.raiz,bg="#F4E8F4", textvariable=self.mensa,font=self.fuente, foreground='blue')
        self.usuario = StringVar()
        self.clave = StringVar()
        self.ctext1 = Entry(self.raiz,bg="#F4E8F4",border=2, textvariable=self.usuario, width=30)
        self.ctext2 = Entry(self.raiz ,bg="#F4E8F4", border=2,textvariable=self.clave, width=30, show="*")
        self.separ1 = ttk.Separator (self.raiz,  orient=HORIZONTAL  ,style='My.TFrame')

        self.boton1 = Button(self.raiz, padx=10, bd=5, text="to Accept", bg="purple", fg="white", cursor="hand1",command=self.valida)
        self.boton2 = Button(self.raiz,padx=15, bd=5, text="Cancel", bg="purple", fg="white",cursor="hand1",command=quit)
        self.raiz.configure(background="#F4E8F4")
        self.img=PhotoImage(file="C:/Users/JANUS/Desktop/andres tachack/proyectos/mai.png")
        can.create_image(20,20,image=self.img,anchor=NW)
        can.configure(background="#F4E8F4")

        self.etiq1.place(x=70, y=140)
        self.etiq2.place(x=30, y=180)
        self.etiq3.place(x=150, y=220)
        self.ctext1.place(x=150, y=142)
        self.ctext2.place(x=150, y=182)
        self.separ1.place(x=5, y=245, bordermode=OUTSIDE,height=10, width=420)
        self.boton1.place(x=150, y=260)
        self.boton2.place(x=240, y=260)

        self.ctext1.focus_set()

        self.ctext2.bind('<button-1>', self.borrar_mensa)
        self.raiz.mainloop()


    def valida(self):
        if self.clave.get() == 'tkinter':
            self.etiq3.configure(foreground='blue')
            self.mensa.set("Acceso permitido")
        else:
            self.etiq3.configure(foreground='red')
            self.mensa.set("Acceso denegado")

    def borrar_mensa(self, evento):
        self.clave.set("")
        self.mensa.set("")

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
