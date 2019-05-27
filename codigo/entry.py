from tkinter import *

#Config de la raiz
root = Tk()

label = Label(root, text="Usuario MAI")
label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

entry = Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

label2 = Label(root, text="Nro. Identificación")
label2.grid(row=1, column=0, sticky="e", padx=10, pady=10)


entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

label3 = Label(root, text="Password")
label3.grid(row=2, column=0, sticky="e", padx=10, pady=10)


entry3 = Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=10)

label4 = Label(root, text="Cargo")
label4.grid(row=3, column=0, sticky="e", padx=10, pady=10)


entry4 = Entry(root)
entry4.grid(row=3, column=1, padx=10, pady=10)

label5 = Label(root, text="E-mail")
label5.grid(row=4, column=0, sticky="e", padx=10, pady=10)


entry5 = Entry(root)
entry5.grid(row=4, column=1, padx=10, pady=10)

label6 = Label(root, text="Rol")
label6.grid(row=5, column=0, sticky="e", padx=10, pady=10)


entry6 = Entry(root)
entry6.grid(row=5, column=1, padx=10, pady=10)



root.mainloop()