#Crear una aplicación que permita realizar la venta de productos. Se debe de ingresar el
#nombre del Cliente, el producto, precio unitario y cantidad a llevar. 
#En caso se realice la compra de más de 5 unidades del producto 
#descontarle el 10% del monto total a pagar.

# monto total = Precio unitario X Cantidad Total (si es mas de 5 unidades hacer un 10% de descuento)

from tkinter import Tk, Label, Entry, Button

#Ajustes a la Ventana Grafica
ventana = Tk()
ventana.geometry("400x300")
ventana.resizable(0,0)
ventana.title("Venta de Productos")

Label(ventana, text="Venta", font="48px").pack()

#Nombre del Cliente
Label(ventana, text="Nombre del Cliente", font="24px").place(x = 30, y = 50)
txtName = Entry(ventana, border="2px")
txtName.place(x = 180, y = 50, width="100px")

#Nombre del Producto
Label(ventana, text="Producto", font="24px").place(x = 30, y = 80)
txtProd = Entry(ventana, border="2px")
txtProd.place(x = 180, y = 80, width="100px",)

#Precio por Unidad
Label(ventana, text="Precio X Unidad", font="24px").place(x = 30, y = 110)
txtProd = Entry(ventana, border="2px")
txtProd.place(x = 180, y = 110, width="100px",)

#Cantidad Total
Label(ventana, text="Cantidad Total", font="24px").place(x = 30, y = 140)
txtProd = Entry(ventana, border="2px")
txtProd.place(x = 180, y = 140, width="100px",)


##Buttons
Button(ventana, text="Realizar compra", width=15).place(x=30, y=180)
#Mostrar Ventana Grafica
ventana.mainloop() 

