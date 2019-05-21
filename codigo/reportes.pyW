from tkinter import *
import os
import sys
import psycopg2

root = Tk()
root.state("zoomed")
root.geometry("900x600")
root.title("Medicinae Apparatu Inventory")
root.iconbitmap('med.ico')
root.config(cursor="hand2",bg="#f0f0f0")
conn = psycopg2.connect(database="MAI", user="postgres", host="localhost", password="andetach2014", port="5432")
cur = conn.cursor()
#usuario
root.usuario = os.sys.argv[1]
#Frame informacion del cliente 
informacion = Frame(root, width=900, height=40,bg="#650090",bd=3, relief="groove").pack(fill='x')

#Nombre de la empresa dentro del frame
nombre_cliente = Label(informacion, text= "REPORTES")
nombre_cliente.place(x=10,y=6)
nombre_cliente.config(bg="#650090", fg="white", font=("Courier New",13))

#Ventana principal
def principal():
    os.system("start PRINCIPAL.pyW "+ root.usuario)
    root.destroy()
#Botones de navegacion
navegacion_inferior = Frame(root, width=400, height= 35)
navegacion_inferior.pack(side="bottom",fill='x')
navegacion_inferior.config(bg="#650090", relief="groove")

atras = Button(navegacion_inferior, text="volver", relief="flat", command= principal)
atras.grid(row=0,column=0, padx=(30))
atras.config(bg="#650090", fg="white",font=("Courier New",13))

botton_hoja_vida = Button(navegacion_inferior, text="Hojas de Vida", relief="flat")
botton_hoja_vida.grid(row=0,column=2, padx=(30))
botton_hoja_vida.config(bg="#650090", fg="white",font=("Courier New",13))

botton_ordenes_compra = Button(navegacion_inferior, text="Ordenes de compra", relief="flat")
botton_ordenes_compra.grid(row=0,column=4, padx=(30))
botton_ordenes_compra.config(bg="#650090", fg="white",font=("Courier New",13))

botton_Activos_fijos = Button(navegacion_inferior, text="Activos Fijos", relief="flat")
botton_Activos_fijos.grid(row=0,column=6, padx=(30))
botton_Activos_fijos.config(bg="#650090", fg="white",font=("Courier New",13))


root.mainloop()
