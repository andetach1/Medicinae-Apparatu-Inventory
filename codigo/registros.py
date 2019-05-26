from tkinter import *
import sys, re
from tkinter import ttk
import tkinter as tki


rootR = Tk()
rootR.state("zoomed")
rootR.geometry("900x600")
rootR.title("registros")
rootR.iconbitmap('med.ico')
rootR.config(cursor="hand2",bg="#f0f0f0")

configuracion_tittle = Frame(rootR, width=900, height=40,bg="#650090",bd=3, relief="groove").pack(fill='x')

contorno = Frame(rootR, width=1200, height= 700)
contorno.pack(fill='y',pady=30)
contorno.config(relief="groove")

nombre_equipo = Label(contorno, text="Nombre de equipo biomedico:")
nombre_equipo.grid(row=0,column=0, sticky="e", padx=5, pady=5)
nombre_equipo.config(bd=1, font=("Courier New",13))

nombre_equipo_entry = Entry(contorno)
nombre_equipo_entry.grid(row=0, column=1, padx=5, pady=5)
nombre_equipo_entry.config(bd=1, font=("Courier New",13))
#---------------------------------------------------------------------
marca_equipo = Label(contorno, text="Marca:")
marca_equipo.grid(row=1,column=0, sticky="e", padx=5, pady=5)
marca_equipo.config(bd=1, font=("Courier New",13))

marca_equipo_entry = Entry(contorno)
marca_equipo_entry.grid(row=1, column=1, padx=5, pady=5)
marca_equipo_entry.config(bd=1, font=("Courier New",13))
#---------------------------------------------------------------------
serial_equipo = Label(contorno, text="Serial de equipo:")
serial_equipo.grid(row=2,column=0, sticky="e", padx=5, pady=5)
serial_equipo.config(bd=1, font=("Courier New",13))

serial_equipo_entry = Entry(contorno)
serial_equipo_entry.grid(row=2, column=1, padx=5, pady=5)
serial_equipo_entry.config(bd=1, font=("Courier New",13))
#---------------------------------------------------------------------
fabricante_equipo = Label(contorno, text="Fabricante de equipo:")
fabricante_equipo.grid(row=3,column=0, sticky="e", padx=5, pady=5)
fabricante_equipo.config(bd=1, font=("Courier New",13))

fabricante_equipo_entry = Entry(contorno)
fabricante_equipo_entry.grid(row=3, column=1, padx=5, pady=5)
fabricante_equipo_entry.config(bd=1, font=("Courier New",13))
#---------------------------------------------------------------------

año_fabricante_equipo = Label(contorno, text="Año de fabricación:")
año_fabricante_equipo.grid(row=4,column=0, sticky="e", padx=5, pady=5)
año_fabricante_equipo.config(bd=1, font=("Courier New",13))

fabricante_equipo_entry = Entry(contorno)
fabricante_equipo_entry.grid(row=4, column=1, padx=5, pady=5)
fabricante_equipo_entry.config(bd=1, font=("Courier New",13))

#---------------------------------------------------------------------

ano_equipo = Label(contorno, text="Consultorio:")
ano_equipo.grid(row=5,column=0, sticky="e", padx=5, pady=5)
ano_equipo.config(bd=1, font=("Courier New",13))

ano_equipo_entry = Entry(contorno)
ano_equipo_entry.grid(row=5, column=1, padx=5, pady=5)
ano_equipo_entry.config(bd=1, font=("Courier New",13))
#---------------------------------------------------------------------
activo_equipo = Label(contorno, text="Activo fijo de equipo:")
activo_equipo.grid(row=6,column=0, sticky="e", padx=5, pady=5)
activo_equipo.config(bd=1, font=("Courier New",13))

activo_equipo_entry = Entry(contorno)
activo_equipo_entry.grid(row=6, column=1, padx=5, pady=5)
activo_equipo_entry.config(bd=1, font=("Courier New",13))
#---------------------------------------------------------------------
ubicacion = Label(contorno, text="Ubicación de equipo:")
ubicacion.grid(row=7,column=0, sticky="e", padx=5, pady=5)
ubicacion.config(bd=1, font=("Courier New",13))


ubicacion_equipo_entry = Entry(contorno)
ubicacion_equipo_entry.grid(row=7, column=1, padx=5, pady=5)
ubicacion_equipo_entry.config(bd=1, font=("Courier New",13))


#---------------------------------------------------------------------
requiere_calibracion = Label(contorno, text="¿Requiere calibración?")
requiere_calibracion.grid(row=0,column=3, sticky="w", padx=5, pady=5)
requiere_calibracion.config(bd=1, font=("Courier New",13))

obtener1 = tki.IntVar()

datos = tki.Radiobutton(contorno, text='Si',variable=obtener1,value=1)
datos.grid(row=1,column=3, sticky="w", padx=5, pady=5)

datos2 = tki.Radiobutton(contorno, text='No', variable=obtener1,value=2)
datos2.grid(row=1,column=4, sticky="w", padx=5, pady=5)


#---------------------------------------------------------------------

requiere_mantenimiento = Label(contorno, text="¿Requiere mantenimiento?")
requiere_mantenimiento.grid(row=2,column=3, sticky="w", padx=5, pady=5)
requiere_mantenimiento.config(bd=1, font=("Courier New",13))

obtener2 = tki.IntVar()

datos_mantenimiento = tki.Radiobutton(contorno, text='Si',variable=obtener2,value=1)
datos_mantenimiento.grid(row=3,column=3, sticky="w", padx=5, pady=5)

datos_mantenimiento = tki.Radiobutton(contorno, text='No', variable=obtener2,value=2)
datos_mantenimiento.grid(row=3,column=4, sticky="w", padx=5, pady=5)

#---------------------------------------------------------------------

accessorios_equipo = Label(contorno, text="Accesosrios")
accessorios_equipo.grid(row=5,column=3, sticky="w", padx=5, pady=5)
accessorios_equipo.config(bd=1, font=("Courier New",13))

obtener3 = tki.IntVar()

datos_accesorios = tki.Radiobutton(contorno, text='Si',variable=obtener3,value=1)
datos_accesorios.grid(row=6,column=3, sticky="w", padx=5, pady=5)

datos_accesorios = tki.Radiobutton(contorno, text='No', variable=obtener3,value=2)
datos_accesorios.grid(row=6,column=4, sticky="w", padx=5, pady=5)

serial_accesorio = Label(contorno, text="Serial accesorio")
serial_accesorio.grid(row=7,column=3, sticky="w", padx=5, pady=5)
serial_accesorio.config(bd=1, font=("Courier New",13))

serial_accesorio = Entry(contorno)
serial_accesorio.grid(row=8, column=3, padx=5, pady=5)
serial_accesorio.config(bd=1, font=("Courier New",13))

nombre_accesorio = Label(contorno, text="Nombre accesorio")
nombre_accesorio.grid(row=7,column=4, sticky="w", padx=5, pady=5)
nombre_accesorio.config(bd=1, font=("Courier New",13))

nombre_accesorio = Entry(contorno)
nombre_accesorio.grid(row=8, column=4, padx=5, pady=5)
nombre_accesorio.config(bd=1, font=("Courier New",13))
#---------------------------------------------------------------------


descripcion = Label(contorno, text="Descripción del equipo:")
descripcion.grid(row=8,column=0, sticky="e", padx=5, pady=5)
descripcion.config(bd=1, font=("Courier New",13))

descripcion_texto = Text(contorno)
descripcion_texto.grid(row=9,column=1,sticky="se", padx=5, pady=5)
descripcion_texto.config(bd=1, font=("Courier New",13),width=30, height=10)


#---------------------------------------------------------------------
navegacion_inferior = Frame(rootR, width=400, height= 35)
navegacion_inferior.pack(side="bottom",fill='x')
navegacion_inferior.config(bg="#650090", relief="groove")

atras = Button(navegacion_inferior, text="Cancelar", relief="flat")
atras.grid(row=0,column=1, padx=(30))
atras.config(bg="#650090", fg="white",font=("Courier New",13))

guardar_informacion = Button(navegacion_inferior, text="Guardar", relief="flat")
guardar_informacion.grid(row=0,column=2, padx=(30))
guardar_informacion.config(bg="#650090", fg="white",font=("Courier New",13))

rootR.mainloop()
