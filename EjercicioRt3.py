#============EJERCICIO RETADOR #3=====================#
#Manejo de operadores

#Camiones que trasportan un máx de 3,254 kg
#no se realizan entregas cuando el peso total sea menor al 50% de la capacidad ni cuyo peso exceda la capacidad maxima
#Cemento-40kg c/u | Yeso-30kg c/u
CargaTotal=3254
cementounit=40
yesounit=30
#Preguntar
numcoscem=int(input("Número de costales de cemento: "))
numcosyeso=int(input("Número de costales de yeso: "))

#Realizar calculos
Calculo=(numcoscem*40)+(numcosyeso*30)

print('\n')
#Imprimir resultados
print("El peso total en kg es: ", Calculo )
#Comparación del envio
envio= (CargaTotal/2)<Calculo and CargaTotal>=Calculo 
print("¿Se puede realizar el envío? ", envio )
