#============EJERCICIO RETADOR #4=====================#
#Manejo de operadores

#Lista de productos
Productos=[[1,"Maíz Grano", 285.55], [2,"Pepino", 334.72 ],[3, "Tomate verde", 129]]
Envio=1500
print("Productos Disponibles"+'\n'
     "1--->"+Productos[0][1]+'\n'
     "2--->"+Productos[1][1]+'\n'
     "3--->"+Productos[2][1]+'\n')
idproventa=int(input("Ingrese el Id del producto: "))
numcaja=int(input("Cantidad de cajas a vender: "))
print('\n')

print("===Resultado==")
if idproventa == 1 and numcaja>100:
  print("Producto: "+Productos[0][1])
  print("Precio unitario: $"+str(Productos[0][2] ))
  Total=numcaja*Productos[0][2]
  print("Total: $"+str(Total ))
elif idproventa == 1 and numcaja<=100:
  print("Producto: "+Productos[0][1])
  print("Precio unitario: $"+str(Productos[0][2] ))
  Total=numcaja*Productos[0][2]
  print("Subtotal: $"+str(Total ))
  print("Costo Envio: $1500")
  print("Total: $"+str(Envio+Total))  
elif  idproventa == 2 and numcaja>100:
  print("Producto: "+Productos[1][1])
  print("Precio unitario: $"+str(Productos[1][2] ))
  Total=numcaja*Productos[1][2]
  print("Total: $"+str(Total ))
elif idproventa == 2 and numcaja<=100:
  print("Producto: "+Productos[1][1])
  print("Precio unitario: $"+str(Productos[1][2] ))
  Total=numcaja*Productos[1][2]
  print("Subtotal: $"+str(Total ))
  print("Costo Envio: $1500")
  print("Total: $"+str(Envio+Total))  
elif  idproventa == 3 and numcaja>100:
  print("Producto: "+Productos[2][1])
  print("Precio unitario: $"+str(Productos[2][2] ))
  Total=numcaja*Productos[2][2]
  print("Total: $"+str(Total ))
elif idproventa == 3 and numcaja<=100:
  print("Producto: "+Productos[2][1])
  print("Precio unitario: $"+str(Productos[2][2] ))
  Total=numcaja*Productos[2][2]
  print("Subtotal: $"+str(Total ))
  print("Costo Envio: $1500")
  print("Total: $"+str(Envio+Total))  

