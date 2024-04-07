from tkinter import Tk, Label, Entry, Button, messagebox, ttk, Radiobutton, IntVar
import pymysql

def mostrar():
    query = "SELECT * FROM ALUMNO"
    c.execute(query)
    datos = c.fetchall()
    
    for item in tvCursos.get_children():
        tvCursos.delete(item)
    
    for reg in datos:
        tvCursos.insert("", "end", text=reg[0], values=(reg[1], reg[2], reg[3], reg[4], reg[5]))   
    contar_alumnos()

def contar_alumnos():
    query = "SELECT COUNT(*) FROM ALUMNO"
    c.execute(query)
    cantidad_alumnos = c.fetchone()[0]
    lblResultado.config(text=f"{cantidad_alumnos}")

def registrar():
    try:
        query = "INSERT INTO ALUMNO VALUES(%s, %s, %s, %s, %s, %s)"
        codigo = int(txtCodigo.get())
        apellidos = txtApellidos.get()
        nombres = txtNombres.get()
        sexo = opcion.get()
        if sexo == 1:
            sexo = 'Masculino'
        elif sexo == 2:
            sexo = 'Femenino'
        carrera = txtCarrera.get()
        edad = int(txtEdad.get())  
        
        c.execute(query, (codigo, apellidos, nombres, sexo, carrera, edad))
        db.commit()
        messagebox.showinfo(message="Alumno registrado exitosamente.")
        mostrar()
        
    except Exception as ex:
        messagebox.showerror(message=ex)
          
def modificar():
    try:
        query = "UPDATE ALUMNO SET APELLIDOS=%s, NOMBRES=%s, CARRERA=%s, EDAD=%s WHERE CODIGO=%s"
        codigo = int(txtCodigo.get())
        apellidos = txtApellidos.get()
        nombres = txtNombres.get()
        carrera = txtCarrera.get()
        edad = int(txtEdad.get())    
        
        c.execute(query,(apellidos,nombres,carrera,edad,codigo))
        db.commit()
        messagebox.showinfo(message="Alumno actualizado exitosamente.")
        mostrar()
        
    except Exception as ex:
        messagebox.showerror(message=ex) 

def eliminar():
    try:
        query = "DELETE FROM ALUMNO WHERE CODIGO=%s"
        codigo = int(txtCodigo.get())  
        
        c.execute(query,codigo)
        db.commit()
        messagebox.showinfo(message="Alumno eliminado exitosamente.")
        mostrar()
        
    except Exception as ex:
        messagebox.showerror(message=ex) 

def nuevo():
    txtCodigo.delete(0,"end")
    txtApellidos.delete(0,"end")
    txtNombres.delete(0,"end")
    opcion.set(0)
    txtCarrera.delete(0,"end")
    txtEdad.delete(0,"end")
    txtCodigo.focus()

ventana = Tk()
ventana.geometry("650x450")
Label(ventana, text="CONTROL DE ALUMNOS", font="56px").place(x=220, y=20)

Label(ventana, text="Código:").place(x=10, y=50)
txtCodigo = Entry(ventana)
txtCodigo.place(x=10, y =75)

Label(ventana, text="Nombres:").place(x=10, y=100)
txtNombres = Entry(ventana)
txtNombres.place(x=10, y=125, width="210")

Label(ventana, text="Apellidos:").place(x=10, y=150)
txtApellidos = Entry(ventana)
txtApellidos.place(x=10, y=175, width="210")

Label(ventana, text="Sexo:").place(x=10, y=200)
opcion = IntVar()
Radiobutton(ventana, text="Masculino", value=1).place(x=10, y=220)
Radiobutton(ventana, text="Femenino", value=2).place(x=100, y=220)

Label(ventana, text="Carrera:").place(x=10, y=250)
txtCarrera = Entry(ventana)
txtCarrera.place(x=10, y=270, width="210")

Label(ventana, text="Edad:").place(x=10, y=300)
txtEdad = Entry(ventana)
txtEdad.place(x=10, y=320, width="210")

Label(ventana, text="Total alumnos: ").place(x=510, y=400)
lblResultado = Label(ventana, text="text")
lblResultado.place(x=600, y=400)

Button(ventana, text="Eliminar", width=7, command=eliminar).place(x=160, y=70)
Button(ventana, text="Registrar", width=8, command=registrar).place(x=10, y=370)
Button(ventana, text="Modificar", width=8, command=modificar).place(x=80, y=370)
Button(ventana, text="Nuevo", width=8, command=nuevo).place(x=150, y=370)
Button(ventana, text="Mostrar", width=8, command=mostrar).place(x=565, y=290)

tvCursos = ttk.Treeview(columns=("col1", "col2", "col3","col4","col5"))
tvCursos.column("#0", width=60)
tvCursos.column('col1', width=90)
tvCursos.column('col2', width=60)
tvCursos.column('col3', width=60)
tvCursos.column('col4', width=60)
tvCursos.column('col5', width=60)

tvCursos.heading("#0", text="Código")
tvCursos.heading("col1", text="Apellidos")
tvCursos.heading("col2", text="Nombres")
tvCursos.heading("col3", text="Sexo")
tvCursos.heading("col4", text="Carrera")
tvCursos.heading("col5", text="Edad")
tvCursos.place(x=240, y=50)

try:
    db = pymysql.connect(host="localhost", user="root", password="", db="UNIVERSIDAD")
    messagebox.showinfo(message="Conectado con la DDBB")
    c = db.cursor()  
except Exception as ex:
    messagebox.showerror(message=ex)
    
contar_alumnos()  # Para mostrar la cantidad de alumnos al iniciar la aplicación

ventana.mainloop()
