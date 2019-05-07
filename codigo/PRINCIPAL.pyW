Al aire librefrom tkinter import *

root = Tk()
root.state("zoomed")
root.geometry("900x600")
root.title("Medicinae Apparatu Inventory")
root.iconbitmap('med.ico')
root.config(cursor="hand2",bg="#f0f0f0")




#Frame informacion del cliente 
informacion = Frame(root, width=900, height=40,bg="#650090",bd=3, relief="groove").pack(fill='x')

#Nombre de la empresa dentro del frame
nombre_cliente = Label(informacion, text="Harold Emmanuel Navas")
nombre_cliente.place(x=4,y=6)
nombre_cliente.config(bg="#650090", fg="white", font=("Courier New",13))


#Frame separador
separador = Frame(root, width=170, height=600,bg="#650090",bd=1, relief="groove").pack(anchor="w", fill='y',expand='1')

#botones de navegacion
botton_bloqueo = Button(separador, text="Bloquear", relief="flat")
botton_bloqueo.place(x=8, y=60)
botton_bloqueo.config(bg="#650090", fg="white",font=("Courier New",13))

botton_reportes = Button(separador, text="Reportes", relief="flat")
botton_reportes.place(x=8, y=550)
botton_reportes.config(bg="#650090", fg="white",font=("Courier New",13))

botton_inventario = Button(separador, text="Inventario", relief="flat")
botton_inventario.place(x=8, y=600)
botton_inventario.config(bg="#650090", fg="white",font=("Courier New",13))

botton_reportes = Button(separador, text="Reportes", relief="flat")
botton_reportes.place(x=8, y=650)
botton_reportes.config(bg="#650090", fg="white",font=("Courier New",13))

botton_configuracion = Button(separador, text="Configuración", relief="flat")
botton_configuracion.place(x=8, y=700)
botton_configuracion.config(bg="#650090", fg="white",font=("Courier New",13))



#Frame para los Botones de navegación de la aplicación
navegacion_inferior = Frame(root, width=400, height= 30)
navegacion_inferior.pack(side="bottom",fill='x')
navegacion_inferior.config(bg="#650090", relief="groove")
#Finalizacion
root.mainloop()
