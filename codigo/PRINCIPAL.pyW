from tkinter import *
import os
import sys
import psycopg2
root = Tk()
root.state("zoomed")
root.geometry("900x700")
root.title("Medicinae Apparatu Inventory")
root.iconbitmap('med.ico')
root.config(cursor="hand2",bg="#f0f0f0")
conn = psycopg2.connect(database="MAI", user="postgres", host="localhost", password="andetach2014", port="5432")
cur = conn.cursor()

#Frame informacion del cliente 
informacion = Frame(root, width=900, height=40,bg="#650090",bd=3, relief="groove").pack(fill='x')

#Nombre de la empresa dentro del frame
usuario = os.sys.argv[1]
sqlquery = "select nombre_sede from sedes where cons = (select sede from usuarios where login ilike '" + usuario + "')"
cur.execute(sqlquery)
sucursal=cur.fetchone()
nombre_cliente = Label(informacion, text=sucursal)
                       
nombre_cliente.place(x=4,y=6)
nombre_cliente.config(bg="#650090", fg="white", font=("Courier New",13))

Logo = PhotoImage(file="logo_principal.gif")
Label(root, image=Logo).pack(fill='both',expand='1')

def bloquear():
        os.system("start login.py ")
        root.destroy()
        
def abrir_reportes():
	ventana1 = Tk()
	ventana1.geometry("1200x650")
	ventana1.title("Medicinae Apparatu Inventory")
	ventana1.iconbitmap('med.ico')
	ventana1.config(cursor="hand2",bg="#f0f0f0")

	#Centrado de la ventana reportes

	ventana1.update_idletasks()
	width = ventana1.winfo_width()
	height = ventana1.winfo_height()
	x = (ventana1.winfo_screenwidth() // 2) - (width // 2)
	y = (ventana1.winfo_screenheight() // 2) - (height // 2)
	ventana1.geometry('{}x{}+{}+{}'.format(width, height, x, y))
	
	informacion_reportes = Frame(ventana1, width=900, height=40,bg="#650090",bd=3, relief="groove").pack(fill='x')

	nombre_reportes = Label(ventana1, text="reportes")
	nombre_reportes.place(x=4,y=6)
	nombre_reportes.config(bg="#650090", fg="white", font=("Courier New",13))

	navegacion_inferior1 = Frame(ventana1, width=400, height= 30)
	navegacion_inferior1.pack(side="bottom",fill='x')
	navegacion_inferior1.config(bg="#650090", relief="groove")

	botton_bloqueo = Button(navegacion_inferior1, text="Imprimir hoja de vida", relief="flat")
	botton_bloqueo.place(x=100)
	botton_bloqueo.config(bg="#650090", fg="white",font=("Courier New",13))
	
	botton_reportes = Button(navegacion_inferior1, text="Imprimir orden de compra", relief="flat",command=abrir_reportes)
	botton_reportes.place(x=400)
	botton_reportes.config(bg="#650090", fg="white",font=("Courier New",13))
	
	botton_bajas = Button(navegacion_inferior1, text="Dar de baja ha equipos", relief="flat")
	botton_bajas.place(x=700)
	botton_bajas.config(bg="#650090", fg="white",font=("Courier New",13))

	ventana1.mainloop()
	#botones de navegación

#Frame para los Botones de navegación de la aplicación
navegacion_inferior = Frame(root, width=400, height= 30)
navegacion_inferior.pack(side="bottom",fill='x')
navegacion_inferior.config(bg="#650090", relief="groove")

#botones de navegacion
botton_bloqueo = Button(navegacion_inferior, text="Bloquear", relief="flat", command= bloquear)
botton_bloqueo.place(x=100)
botton_bloqueo.config(bg="#650090", fg="white",font=("Courier New",13))

botton_reportes = Button(navegacion_inferior, text="Reportes", relief="flat",command= abrir_reportes)
botton_reportes.place(x=300)
botton_reportes.config(bg="#650090", fg="white",font=("Courier New",13))

botton_inventario = Button(navegacion_inferior, text="Inventario", relief="flat")
botton_inventario.place(x=500)
botton_inventario.config(bg="#650090", fg="white",font=("Courier New",13))

botton_reportes = Button(navegacion_inferior, text="Registro", relief="flat")
botton_reportes.place(x=700)
botton_reportes.config(bg="#650090", fg="white",font=("Courier New",13))

botton_configuracion = Button(navegacion_inferior, text="Configuración", relief="flat")
botton_configuracion.place(x=900)
botton_configuracion.config(bg="#650090", fg="white",font=("Courier New",13))

#
#Finalizacion
root.mainloop()
