# Crear una aplicación que permita realizar la venta de productos. 
# Se debe de ingresar :
# * Nombre del Cliente
# * Producto 
# * Precio unitario 
# * Cantidad a llevar. 
# En caso se realice la compra de más de 5 unidades del producto 
# Descontarle el 10% del monto total a pagar.
# monto total = Precio unitario X Cantidad  (si es mas de 5 unidades hacer un 10% de descuento)

from tkinter import Tk, Label, Entry, Button

### Funciones

def montoTotal() :
    precio = float(txtPrecu.get())
    cantidad = float(txtCantidad.get())
    montoAPagar = precio * cantidad

    # Aplicar descuento del 10% si la cantidad es mayor a 5
    if cantidad > 5:
        descuento = montoAPagar * 0.10
        montoAPagar -= descuento

    montoAPagar = round(montoAPagar, 2)
    lblResultado["text"] = montoAPagar


# Ajustes a la Ventana Grafica
ventana = Tk()
ventana.geometry("400x300")
ventana.resizable(0, 0)
ventana.title("Venta de Productos")

### Labels

Label(ventana, text="Venta", font="48px").pack()
# Nombre del Cliente
Label(ventana, text="Nombre del Cliente", font="24px").place(x=30, y=50)
txtName = Entry(ventana, border="2px")
txtName.place(x=180, y=50, width="100px")

# Nombre del Producto
Label(ventana, text="Producto", font="24px").place(x=30, y=80)
txtProd = Entry(ventana, border="2px")
txtProd.place(x=180, y=80, width="100px")

# Cantidad Total
Label(ventana, text="Cantidad", font="24px").place(x=30, y=110)
txtCantidad = Entry(ventana, border="2px")
txtCantidad.place(x=180, y=110, width="100px")

# Precio por Unidad
Label(ventana, text="Precio X Unidad", font="24px").place(x=30, y=140)
txtPrecu = Entry(ventana, border="2px")
txtPrecu.place(x=180, y=140, width="100px")

# Mostrando cantidad a pagar
Label(ventana, text="Usted debe pagar: ").place(x=40, y=220)
lblResultado = Label(ventana, text=".....")
lblResultado.place(x=140, y=220)

### Buttons
Button(ventana, text="Calcular compra", width=15, border="2px", command=montoTotal).place(x=30, y=180)

# Mostrar Ventana Grafica
ventana.mainloop()




