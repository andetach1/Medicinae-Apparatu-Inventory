from tkinter import *

#COnfiguración de la raiz 
root = Tk()
#root.state("zoomed")
root.geometry("900x600")
root.title("Medicinae Apparatu Inventory")
root.iconbitmap('med.ico')


#Frame contenedor
Contenedor_principal = Frame(root,width=480, height= 300)
Contenedor_principal.pack(fill='both',expand='1')
Contenedor_principal.config(bg="#E6CDF0",bd=5, relief="groove")



#Barra superior donde se muestra el nombre de la empresa
info_empresa = Frame(Contenedor_principal, width=400, height= 50)
info_empresa.pack(fill='x')
info_empresa.config(bg="#650090",bd=2, relief="groove")


#Etiqueta donde se muestra el nombre de empresa
nombre_empresa = Label(info_empresa, text="Harold Emmanuel Navas")
nombre_empresa.place(x=5,y=5)
nombre_empresa.config(bg="#650090", fg="white", font=("Courier New",22))

#Etiqueta Logotipo
Logo = PhotoImage(file="logo_principal.gif")
Label(Contenedor_principal, image=Logo).pack(fill='both',expand='1')

#Frame para los Botones de navegación de la aplicación
navegacion_inferior = Frame(Contenedor_principal, width=400, height= 60)
navegacion_inferior.pack(side="bottom",fill='x')
navegacion_inferior.config(bg="#f0e8f3", relief="groove")

image_button_home = PhotoImage(file="home.gif")
Boton_home = Button(navegacion_inferior, text="Home", image=image_button_home, height = 80 ,width=80)
Boton_home.place(x=5,y=5)
Boton_home.grid(row=0,column=0)
Boton_home.config(bg="#f0e8f3", relief="groove", bd=0)
nombre_home = Label(Boton_home, text="Home")
nombre_home.pack()


Boton_reportes = Button(navegacion_inferior, text="Reportes")
Boton_reportes.place(x=5,y=20)
Boton_reportes.grid(row=0,column=1)

boton_inventario = Button(navegacion_inferior, text="inventario")
boton_inventario.place(x=5,y=5)
boton_inventario.grid(row=0,column=2)

boton_registros = Button(navegacion_inferior, text="Registros")
boton_registros.place(x=5,y=5)
boton_registros.grid(row=0,column=3)

boton_configuracion = Button(navegacion_inferior, text="Configuración")
boton_configuracion.place(x=5,y=5)
boton_configuracion.grid(row=0,column=4)

boton_bloqueo = Button(navegacion_inferior, text="Bloquear")
boton_bloqueo.place(x=5,y=5)
boton_bloqueo.grid(row=0,column=5)







#Final del bucle 
root.mainloop()