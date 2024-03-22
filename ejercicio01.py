#Paso 1 (Obligatorio) : Importat la libreria TKINRTER
from tkinter import Tk, Label, Entry, Button

#Paso 2 (Obligatorio) : Crear una variable de tipo TK
ventana = Tk()

#Paso 3 (Obligatorio) : Agregamos un titulo a la ventana
ventana.title("INTERFAZ GRAFICA CON Tkinter en Python")

#Paso 4 (Segun necesidad) : Agregamos las dimensiones de la ventana
ventana.geometry("600x400")

#Paso 5 : Diseñamos el contenido del formulario
Label(ventana, text="Registro de Estudiantes", font="Arial 16").pack()
Label(ventana, text="Nombre: ").pack()
Entry(ventana).pack()
Label(ventana, text="Edad: ").pack()
Entry(ventana).pack()
Button(ventana, text="Registrar", bg="magenta", fg="#fff").pack()

#Paso Final (Obligatorio) : Ejecutamos la ventana grafica
ventana.mainloop() 
