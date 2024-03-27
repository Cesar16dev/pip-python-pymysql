## Se desea calcular el promedio ponderado en base a los pesos porcentuales de cada curso:
# • Examen Parcial (30%)
# • Examen final (40%)
# • Promedio de Practicas (20%)
# • Promedio de trabajos (10%)

# Importando la libreria Tkinter
from tkinter import Tk, Entry, Label, messagebox, Button

# Funcion para calcular el promedio final
def calcular_promedio():
    # Usando un try-except
    try:
        # Obtener los valores de los campos de texto
        parcial = float(txtParcial.get())
        final = float(txtFinal.get())
        practicas = float(txtPracticas.get())
        trabajos = float(txtTrabajos.get())
        # Sacando Promedio ponderado
        promedio_ponderado = (parcial * 0.30) + (final * 0.40) + (practicas * 0.20) + (trabajos * 0.10)        
        lblResultado["text"] = round(promedio_ponderado,1)
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos en todos los campos.")


# Crear la ventana principal
window = Tk()
window.title("Calculadora de Promedio Ponderado")
window.geometry("500x300")

# Crear etiquetas y campos de texto
Label(window, text="Examen Parcial:", font="36px").place(x=30, y=50)
txtParcial = Entry(window, border="2px")
txtParcial.place(x=220, y=50, width="100px")

Label(window, text="Examen Final:", font="36px").place(x=30, y=80)
txtFinal = Entry(window, border="2px")
txtFinal.place(x=220, y=80, width="100px")

Label(window, text="Promedio de Prácticas:", font="36px").place(x=30, y=110)
txtPracticas = Entry(window, border="2px")
txtPracticas.place(x=220, y=110, width="100px")

Label(window, text="Promedio de Trabajos:", font="36px").place(x=30, y=140)
txtTrabajos = Entry(window, border="2px")
txtTrabajos.place(x=220, y=140, width="100px")

Label(window, text="Su promedio ponderado es: ", font="48px").place(x=40, y=250)
lblResultado = Label(window, text="...", font="48px")
lblResultado.place(x=260, y=250)

# Botón para calcular el promedio
Button(window, text="Calcular Promedio", command=calcular_promedio, width="30", height="1", fg="#00f").place(x=110, y=190)

# Ejecutar el la ventana principal
window.mainloop()
