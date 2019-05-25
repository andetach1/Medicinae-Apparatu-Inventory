from tkinter import *
import sys, re
import os
from tkinter import ttk
import psycopg2

rootC = Tk()
rootC.state("zoomed")
rootC.geometry("1200x600")
rootC.title("Medicinae Apparatu Inventory")
rootC.iconbitmap('med.ico')
rootC.config(cursor="hand2",bg="#f0f0f0")
conn = psycopg2.connect(database="MAI", user="postgres", host="localhost", password="andetach2014", port="5432")
cur = conn.cursor()
#usuario
rootC.usuario = os.sys.argv[1]

def crear_usuarios():
        os.system("start Creacion usuarios.pyW ")
        rootC.destroy()

def vovler():
        os.system("start PRINCIPAL.pyW "+ rootC.usuario)
        rootC.destroy()
	#---------------------------------------------------------------------------

#Frame informacion del cliente 
configuracion_tittle = Frame(rootC, width=900, height=40,bg="#650090",bd=3, relief="groove").pack(fill='x')


#Nombre de la empresa dentro del frame
nombre_cliente = Label(configuracion_tittle, text="CONFIGURACIÓN")
nombre_cliente.place(x=10,y=6)
nombre_cliente.config(bg="#650090", fg="white", font=("Courier New",13))

#Botones de navegacion
navegacion_inferior = Frame(rootC, width=400, height= 35)
navegacion_inferior.pack(side="bottom",fill='x')
navegacion_inferior.config(bg="#650090", relief="groove")

atras = Button(navegacion_inferior, text="volver", relief="flat", command= volver)
atras.grid(row=0,column=0, padx=(30))
atras.config(bg="#650090", fg="white",font=("Courier New",13))

botton_hoja_vida = Button(navegacion_inferior, text="Crear usuarios", relief="flat", command=crear_usuarios)
botton_hoja_vida.grid(row=0,column=2, padx=(30))
botton_hoja_vida.config(bg="#650090", fg="white",font=("Courier New",13))

botton_ordenes_compra = Button(navegacion_inferior, text="Configuración de empresa", relief="flat")
botton_ordenes_compra.grid(row=0,column=4, padx=(30))
botton_ordenes_compra.config(bg="#650090", fg="white",font=("Courier New",13))




rootC.mainloop()
