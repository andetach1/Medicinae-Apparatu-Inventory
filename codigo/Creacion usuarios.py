from tkinter import *
import sys, re
from tkinter import ttk
import psycopg2

conn = psycopg2.connect(database="MAI", user="postgres", host="localhost", password="andetach2014", port="5432")
cur = conn.cursor()


usuarios_nuevos = Tk()
usuarios_nuevos.geometry("800x600")
usuarios_nuevos.title("Creación de usuarios")
usuarios_nuevos.iconbitmap('med.ico')
usuarios_nuevos.config(cursor="hand2",bg="#f0f0f0")
informativo = Label(usuarios_nuevos, text="POR FAVOR INGRESE LOS DATOS DE REGISTRO")
informativo.grid(row=0, column=0, sticky="e",pady=30)
informativo.config(bd=1, font=("Courier New",13))
nombre_usuario = Label(usuarios_nuevos, text="Nombre de usuario:")
nombre_usuario.grid(row=1, column=0, sticky="e")
nombre_usuario.config(bd=1, font=("Courier New",13))
usuarios_nuevos.usuario = os.sys.argv[1]

campo_nombre_usuario = Entry(usuarios_nuevos)
campo_nombre_usuario.grid(row=1, column=1)
campo_nombre_usuario.config(bd=1, font=("Courier New",13))

cedula_usuario = Label(usuarios_nuevos, text="Cedula usuario:")
cedula_usuario.grid(row=2,column=0, sticky="e", padx=5, pady=5)
cedula_usuario.config(bd=1, font=("Courier New",13))
campo_cedula_usuario = Entry(usuarios_nuevos)
campo_cedula_usuario.grid(row=2, column=1, padx=5, pady=5)
campo_cedula_usuario.config(bd=1, font=("Courier New",13))

clave_usuario = Label(usuarios_nuevos, text="Clave usuario:")
clave_usuario.grid(row=1,column=2, sticky="e", padx=5, pady=5)
clave_usuario.config(bd=1, font=("Courier New",13))

campo_clave_primaria = Entry(usuarios_nuevos)
campo_clave_primaria.grid(row=1, column=3, padx=5, pady=5)
campo_clave_primaria.config(bd=1, font=("Courier New",13), show="*")

repetir_clave = Label(usuarios_nuevos, text="confirme clave:")
repetir_clave.grid(row=2,column=2, sticky="e", padx=5, pady=5)
repetir_clave.config(bd=1, font=("Courier New",13))

campo_clave_segundaria = Entry(usuarios_nuevos)
campo_clave_segundaria.grid(row=2, column=3, padx=5, pady=5)
campo_clave_segundaria.config(bd=1, font=("Courier New",13), show="*")


registrar = Button(usuarios_nuevos, text="Registrar", relief="flat")
registrar.grid(row=3,column=4, padx=30,pady=30)
registrar.config(bg="#650090", fg="white",font=("Courier New",13))


def volver() :
     os.system("start PRINCIPAL.pyW "+ usuarios_nuevos.usuario)
    root.destroy()

#Botones de navegacion
navegacion_inferior = Frame(rootC, width=400, height= 35)
navegacion_inferior.pack(side="bottom",fill='x')
navegacion_inferior.config(bg="#650090", relief="groove")

atras = Button(navegacion_inferior, text="volver", relief="flat", command=volver)
atras.grid(row=0,column=0, padx=(30))
atras.config(bg="#650090", fg="white",font=("Courier New",13))
usuarios_nuevos.mainloop()