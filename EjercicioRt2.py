#============EJERCICIO RETADOR #2=====================#
#Índices y listas

#Variables
Municipios=[];#Lista
MunicipioCap="";#Para capturar
Habitantes=[];#Lista
HabitantesCap="";#Para capturar

#Solicitar al usuario ingresar el nombre del municipio y agregarlo a la lista Nota: Solicitarse 3 veces
print( "===========CAPTURAR INFORMACIÓN==========="+'\n')
#--Capturar información
MunicipioCap= input("Escribe el nombre del municipio 1:")
HabitantesCap= input("Escribe el número de habitantes:")
#--Agregar a las listas la info capturada
Municipios.append(MunicipioCap)
Habitantes.append(HabitantesCap)
#--Mostrar la info capturada del municipio (individualmente)
print( '=======Municipio Capturado======'+'\n',
         'Nombre:'+Municipios[0]+'\n',
         'Habitantes:'+Habitantes[0])
print( '\n')

MunicipioCap= input("Escribe el nombre del municipio 2:")
HabitantesCap= input("Escribe el número de habitantes:")
#--Agregar a las listas la info capturada
Municipios.append(MunicipioCap)
Habitantes.append(HabitantesCap)
#--Mostrar la info capturada del municipio (individualmente)
print( '=======Municipio Capturado======'+'\n',
         'Nombre:'+Municipios[1]+'\n',
         'Habitantes:'+Habitantes[1])
print( '\n')

MunicipioCap= input("Escribe el nombre del municipio 3:")
HabitantesCap= input("Escribe el número de habitantes:")
#--Agregar a las listas la info capturada
Municipios.append(MunicipioCap)
Habitantes.append(HabitantesCap)
#--Mostrar la info capturada del municipio (individualmente)
print( '=======Municipio Capturado======'+'\n',
         'Nombre:'+Municipios[2]+'\n',
         'Habitantes:'+Habitantes[2])
print( '\n')

print( "===========INFORMACIÓN GENERAL==========="+'\n')
#Convertir lista de habitantes a int
int_list=[int(i) for i in Habitantes]

TotalH=sum(int_list)
PromedioH=sum(int_list)/len(Habitantes)

print('Total de habitantes: '+str(TotalH))
print('Promedio habitantes: '+str(PromedioH))
