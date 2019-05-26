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
rootC.conn = psycopg2.connect(database="MAI", user="postgres", host="localhost", password="andetach2014", port="5432")
rootC.cur = rootC.conn.cursor()

#usuario
rootC.usuario = os.sys.argv[1]

def crear_usuarios():
  usuarios_nuevos = Tk()
  usuarios_nuevos.geometry("1200x600")
  usuarios_nuevos.title("Creación de usuarios")
  usuarios_nuevos.iconbitmap('med.ico')
  usuarios_nuevos.config(cursor="hand2",bg="#f0f0f0")

  informativo = Label(usuarios_nuevos, text="POR FAVOR INGRESE LOS DATOS DE REGISTRO")
  informativo.grid(row=0, column=0, sticky="e",pady=30)
  informativo.config(bd=1, font=("Courier New",13))

  nombre_usuario = Label(usuarios_nuevos, text="Nombre de usuario:")
  nombre_usuario.grid(row=1, column=0, sticky="e")
  nombre_usuario.config(bd=1, font=("Courier New",13))

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
  mensa = StringVar()
  etiq3 = Label(usuarios_nuevos,bg="#F4E8F4", textvariable=mensa,font=("Courier New",13), foreground='blue')
  etiq3.grid(row=5, column=2, padx=5, pady=5)
  
  campo_clave_segundaria = Entry(usuarios_nuevos)
  campo_clave_segundaria.grid(row=2, column=3, padx=5, pady=5)
  campo_clave_segundaria.config(bd=1, font=("Courier New",13), show="*")
  sucursal= Label(usuarios_nuevos, text="Sucursal asignada:")
  sucursal.grid(row=3,column=0, sticky="e", padx=5, pady=5)
  sucursal.config(bd=1, font=("Courier New",13))
  campo_sucursal = Entry(usuarios_nuevos)
  campo_sucursal.grid(row=3, column=1, padx=5, pady=5)
  campo_sucursal.config(bd=1, font=("Courier New",13))

  def registrar_usuario():
          
          if(campo_clave_primaria.get() == campo_clave_segundaria.get()):
                        sqlquery = "insert into usuarios (login,pwd,cedula,grabador,fecha_grab,sede) values ('"+ campo_nombre_usuario.get() +"','"+ campo_clave_primaria.get() +"','"+ campo_cedula_usuario.get() +"','"+ rootC.usuario +"',now(),"+ campo_sucursal.get() +");"
                        rootC.cur.execute(sqlquery)
                        rootC.conn.commit()
                        print(rootC.cur.statusmessage)
                        mensa.set("Usuario Registrado")
          else:
                        mensa.set("La contraseña no coincide")
      
  def actualizar_usuario():
          
          if(campo_clave_primaria.get() == campo_clave_segundaria.get()):
                        sqlquery = "select cons from usuarios where login ilike '"+ campo_nombre_usuario.get() +"';"
                        rootC.cur.execute(sqlquery)
                        existe=rootC.cur.fetchone()
                        print (existe[0])
                        if(existe != None ):
                                cons= existe[0]
                                sqlquery = "update usuarios set login = '" + campo_nombre_usuario.get() +"',pwd = '"+ campo_clave_primaria.get() +"',cedula = '"+ campo_cedula_usuario.get() +"',grabador = '"+ rootC.usuario +"',fecha_grab = now(),sede = "+ campo_sucursal.get() +"where cons in ("+ str(cons) +");"
                                rootC.cur.execute(sqlquery)
                                rootC.conn.commit()
                                mensa.set("Usuario actualizado")
                        else :
                                mensa.set("El usuario no existe en la base de datos")
          else :
                        mensa.set("La contraseña no coincide")

  registrar = Button(usuarios_nuevos, text="Registrar", relief="flat",command= registrar_usuario)
  registrar.grid(row=4,column=3, padx=30,pady=30)
  registrar.config(bg="#650090", fg="white",font=("Courier New",13))


  actualizar = Button(usuarios_nuevos, text="Actualizar", relief="flat",command= actualizar_usuario)
  actualizar.grid(row=4,column=4, padx=30,pady=30)
  actualizar.config(bg="#650090", fg="white",font=("Courier New",13))


  usuarios_nuevos.mainloop()

def volver():
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
 
