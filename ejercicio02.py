from tkinter import Tk, Label, Entry, Button

def sumar():
    n1 = int(txtNum1.get())
    n2 = int(txtNum2.get())   
    suma = n1 + n2
    lblResultado["text"] = suma

def restar():
    n1 = int(txtNum1.get())
    n2 = int(txtNum2.get())   
    resta = n1 - n2
    lblResultado["text"] = resta

def multiplicar():
    n1 = int(txtNum1.get())
    n2 = int(txtNum2.get())   
    multiplica = n1 * n2
    lblResultado["text"] = multiplica
    
def dividir():
    n1 = int(txtNum1.get())
    n2 = int(txtNum2.get())   
    divide = n1 // n2
    lblResultado["text"] = divide

ventana = Tk()
#Paso 4 (Segun necesidad) : Agregamos las dimensiones de la ventana
ventana.geometry("300x300")
ventana.resizable(0,0)

#Paso 5 : Diseñamos el contenido del Formulario
Label(ventana, text="CALCULADORA").pack()
Label(ventana, text="Numero 1 :").place(x=20, y=50)
txtNum1 = Entry(ventana)
txtNum1.place(x = 90, y=50)

Label(ventana, text="Numero 2 :").place(x=20, y=80)
txtNum2 = Entry(ventana)
txtNum2.place(x = 90, y=80)

Button(ventana, text="+", width=4, command=sumar).place(x=90, y=120)
Button(ventana, text="-", width=4, command=restar).place(x=130, y=120)
Button(ventana, text="*", width=4, command=multiplicar).place(x=170, y=120)
Button(ventana, text="/", width=4, command=dividir).place(x=210, y=120)

Label(ventana, text="Resultado: ").place(x=40, y=160)
lblResultado = Label(ventana, text="text")
lblResultado.place(x=100, y=160)

#Paso Final (Obligatorio) : Ejecutamos la ventana grafica
ventana.mainloop() 