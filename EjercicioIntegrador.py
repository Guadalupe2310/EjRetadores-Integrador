#============PRODUCTO INTEGRADOR=====================#
#Lista de productos y ventas totales
venta_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]]

Productos=[[1,"Maíz Grano", 285.55], 
           [2,"Pepino", 334.72 ],
           [3, "Tomate verde", 129]]

VentasDia=int(0)

#Flujo del programa
print("Productos Disponibles"+'\n'
     "1--->"+Productos[0][1]+'\n'
     "2--->"+Productos[1][1]+'\n'
     "3--->"+Productos[2][1]+'\n')
idproventa=int(input("Ingrese el Id del producto: "))
numcaja=int(input("Cantidad de cajas a vender: "))
print('\n')

#Comparar si entra el costo del envio
if int(numcaja) > 100:
  Envio = float(0)  
  print("No aplica envio")
if int(numcaja) <= 100:
  Envio = float(1500.00)
  print("Envio $1500")

#Sumar las ventas del día de la lista 
for V in range(0,len(venta_productos)):
  Venta = venta_productos[V]
  VentasDia += int(Venta[1]) 
  
#Sumar el total de las ventas del día + lo ingresado
TotalCajasVentas=VentasDia+numcaja
print("Ventas del día del producto: "+str(TotalCajasVentas))
if TotalCajasVentas<1500:
  print("Tiene descuento del 20%")
else:
   print("No aplica descuento")

print('\n')

print("===Resultado==")
for i in range(0, len(Productos)):   
    Producto = Productos[i]
    #Obtener información del producto
    if int(Producto[0])==int(idproventa):
        NomProducto = Producto[1]
        Preciounit = float(Producto[2])
        Subtotal=(Preciounit * float(numcaja))
        SubtotalEnvio = Subtotal+Envio
        #Comparar y aplicar descuento (en caso dé) 
        if TotalCajasVentas<1500:
         SubtotalDesc =Subtotal*0.2
        else:
           SubtotalDesc =0
        #Calcular el total de la venta 
        TotalVentas=Subtotal+SubtotalDesc+SubtotalEnvio

#imorimir resultados obtenidos
print ("Producto: "+ NomProducto)
print ("Precio unitario "+ str(Preciounit))
print ("Subtotal: "+ str(Subtotal))
print ("+Envio ($1500): "+ str(SubtotalEnvio))
print ("+Descuento: "+ str(SubtotalDesc))
print ("Total: "+ str(TotalVentas))