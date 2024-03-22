from tkinter import Tk, Label, Entry, Button, messagebox, ttk

#Importamos la libreria que permite conectarnos con MySQL
import pymysql

ventana = Tk()
ventana.geometry("700x400")
Label(ventana, text="CONTROL DE CURSOS").place(x=200, y=20)

#Labels
Label(ventana, text="ID:").place(x=10, y=50)
txtID = Entry(ventana)
txtID.place(x=10, y =75)

Label(ventana, text="CURSO:").place(x=10, y=100)
txtCurso = Entry(ventana)
txtCurso.place(x=10, y=125, width="210")

Label(ventana, text="CICLO:").place(x=10, y=150)
txtCiclo = Entry(ventana)
txtCiclo.place(x=10, y=175, width="210")

Label(ventana, text="HORAS:").place(x=10, y=200)
txtHoras = Entry(ventana)
txtHoras.place(x=10, y=225, width="210")

#Buttons
Button(ventana, text="Eliminar", width=7).place(x=160, y=70)
Button(ventana, text="Registrar", width=8).place(x=10, y=270)
Button(ventana, text="Modificar", width=8).place(x=80, y=270)
Button(ventana, text="Listar", width=8).place(x=150, y=270)


#TREEVIEW
tvCursos = ttk.Treeview(columns=("col1", "col2", "col3"))
tvCursos.column("#0", width=60)
tvCursos.column('col1', width=250)
tvCursos.column('col2', width=60)
tvCursos.column('col3', width=60)

tvCursos.heading("#0", text="ID")
tvCursos.heading("col1", text="CURSOS")
tvCursos.heading("col2", text="CICLO")
tvCursos.heading("col3", text="HORAS")

tvCursos.place(x=240, y=50)

#Nos conectamos a la BBDD ESCUELA
try:
    db = pymysql.connect(host="localhost", user="root", password="", db="ESCUELA")
    messagebox.showinfo(message="Bien")
    c = db.cursor()  
    
except Exception as ex:
    messagebox.showerror(message = ex)
    
ventana.mainloop()