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
root.usuario = os.sys.argv[1]
sqlquery = "select nombre_sede from sedes where cons = (select sede from usuarios where login ilike '" + root.usuario + "')"
cur.execute(sqlquery)
sucursal=cur.fetchone()
nombre_cliente = Label(informacion, text=sucursal)
                       
nombre_cliente.place(x=4,y=6)
nombre_cliente.config(bg="#650090", fg="white", font=("Courier New",13))

Logo = PhotoImage(file="logo_principal.gif")
Label(root, image=Logo).pack(fill='both',expand='1')

def bloquear():
        os.system("start login.pyW ")
        root.destroy()
        
def abrir_reportes():
        
        os.system("start reportes.pyW "+ root.usuario)
        root.destroy()
	
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
