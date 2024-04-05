from tkinter import Tk, Label, Entry, Button, messagebox, ttk, Radiobutton, IntVar

#Importamos la libreria que permite conectarnos con MySQL
import pymysql

def mostrar():
    query = "SELECT * FROM CURSOS"
    c.execute(query)
    
    #Recuperamos todos los datos
    datos = c.fetchall()
    
    # Evitar la propagacion de datos
    for item in tvCursos.get_children():
        tvCursos.delete(item)
    
    #Mostramos los datos
    for reg in datos:
        tvCursos.insert("","end",text=reg[0], values=(reg[1], reg[2],reg[3]))   


def registrar():
    try:
        query = "INSERT INTO CURSOS VALUES(%s, %s, %s, %s)"
        id = int(txtID.get())
        curso = txtCurso.get()
        ciclo = int(txtCiclo.get())
        horas = int(txtHoras.get())   
        #Ejecutamos la consulta (query)
        c.execute(query,(id,curso,ciclo,horas))
        db.commit()
        messagebox.showinfo(message="Curso registrado exitosamente.")
        mostrar()
        
    except Exception as ex:
        messagebox.showerror(message=ex) 
          
def modificar():
    try:
        query = "UPDATE CURSOS SET CURSO=%s, CICLO=%s, HORAS=%s WHERE IDCURSO=%s"
        id = int(txtID.get())
        curso = txtCurso.get()
        ciclo = int(txtCiclo.get())
        horas = int(txtHoras.get())   
        #Ejecutamos la consulta (query)
        c.execute(query,(curso,ciclo,horas,id))
        db.commit()
        messagebox.showinfo(message="Curso actualizado exitosamente.")
        mostrar()
        
    except Exception as ex:
        messagebox.showerror(message=ex) 

def eliminar():
    try:
        query = "DELETE FROM CURSOS WHERE IDCURSO=%s"
        id = int(txtID.get())  
        
        #Ejecutamos la consulta (query)
        c.execute(query,id)
        db.commit()
        messagebox.showinfo(message="Curso eliminado exitosamente.")
        mostrar()
        
    except Exception as ex:
        messagebox.showerror(message=ex) 

def nuevo():
    txtID.delete(0,"end")
    txtCurso.delete(0,"end")
    txtCiclo.delete(0,"end")
    txtHoras.delete(0,"end")
    txtID.focus()

ventana = Tk()
ventana.geometry("700x400")
Label(ventana, text="CONTROL DE CURSOS").place(x=200, y=20)

#Labels
Label(ventana, text="Código:").place(x=10, y=50)
txtID = Entry(ventana)
txtID.place(x=10, y =75)

Label(ventana, text="Nombres:").place(x=10, y=100)
txtCurso = Entry(ventana)
txtCurso.place(x=10, y=125, width="210")

Label(ventana, text="Apellidos:").place(x=10, y=150)
txtCiclo = Entry(ventana)
txtCiclo.place(x=10, y=175, width="210")

Label(ventana, text="Sexo:").place(x=10, y=200)
opcion = IntVar()
Radiobutton(ventana, text="Masculino", value=1).place(x=10, y=220)
Radiobutton(ventana, text="Femenino", value=2).place(x=90, y=220)

Label(ventana, text="HORAS:").place(x=10, y=300)
txtHoras = Entry(ventana)
txtHoras.place(x=10, y=300, width="210")



#Buttons
Button(ventana, text="Registrar", width=8, command=registrar).place(x=10, y=270)
Button(ventana, text="Eliminar", width=7, command=eliminar).place(x=160, y=70)
Button(ventana, text="Modificar", width=8, command=modificar).place(x=80, y=270)
Button(ventana, text="Nuevo", width=8, command=nuevo).place(x=150, y=270)

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
    messagebox.showinfo(message="Conectado con la DDBB")
    c = db.cursor()  
    
except Exception as ex:
    messagebox.showerror(message = ex)
    
ventana.mainloop()