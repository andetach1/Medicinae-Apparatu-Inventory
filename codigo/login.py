#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import ttk, font
import getpass
import psycopg2
import os
import sys




class Aplicacion():
    def __init__(self):
        conn = psycopg2.connect(database="MAI", user="postgres", host="localhost", password="andetach2014", port="5432")
        self.cur = conn.cursor()
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

        self.boton1 = Button(self.raiz, padx=10, bd=5, text="Aceptar", bg="purple", fg="white", cursor="hand1",command=self.valida)
        self.boton2 = Button(self.raiz,padx=15, bd=5, text="Cancelar", bg="purple", fg="white",cursor="hand1",command=quit)
        self.raiz.configure(background="#F4E8F4")
        self.img=PhotoImage(file="mai.png")
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

       
        self.raiz.mainloop()
    

    def valida(self):
        sqlquery = "select pwd from usuarios where login ilike '" + self.usuario.get() + "'"
        self.cur.execute(sqlquery)
        pwd=self.cur.fetchone()
        
        if self.clave.get() == pwd[0] :
            self.etiq3.configure(foreground='blue')
            self.mensa.set("Acceso permitido")
            os.system("start PRINCIPAL.pyW "+self.usuario.get())
            self.raiz.destroy()
            
           
        else:
            self.etiq3.configure(foreground='red')
            self.mensa.set("Acceso denegado")


def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
