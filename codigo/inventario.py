from tkinter import *
import sys, re
from tkinter import ttk
import tkinter as tki
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

rootR = Tk()
rootR.state("zoomed")
rootR.geometry("900x600")
rootR.title("Inventario general")
rootR.iconbitmap('med.ico')
rootR.config(cursor="hand2",bg="#f0f0f0")

configuracion_tittle = Frame(rootR, width=900, height=40,bg="#650090",bd=3, relief="groove").pack(fill='x')



#---------------------------------------------------------------------
navegacion_inferior = Frame(rootR, width=400, height= 35)
navegacion_inferior.pack(side="bottom",fill='x')
navegacion_inferior.config(bg="#650090", relief="groove")


scrollbar = Scrollbar(rootR)
scrollbar.pack(side=RIGHT, fill='y')

listbox = Text(rootR, yscrollcommand=scrollbar.set)
for i in range(10000):
    listbox.insert(END, str(i))
listbox.pack(fill='both',expand=1)
scrollbar.config(command=listbox.yview)

def imprimir():
	documento = listbox
	c = canvas.Canvas("inventario_prueba.pdf")

	c.drawString(120,760,"Reporte de inventario Medicinae Apparatu Inventory")
	c.drawString(120,780,)
	c.save()


atras = Button(navegacion_inferior, text="Atras", relief="flat")
atras.grid(row=0,column=0, padx=(30))
atras.config(bg="#650090", fg="white",font=("Courier New",13))

imprimir_informacion = Button(navegacion_inferior, text="Imprimir", relief="flat",command=imprimir)
imprimir_informacion.grid(row=0,column=1, padx=(30))
imprimir_informacion.config(bg="#650090", fg="white",font=("Courier New",13))

rootR.mainloop()
