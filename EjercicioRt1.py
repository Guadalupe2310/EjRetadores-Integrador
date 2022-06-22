#============EJERCICIO RETADOR #1=====================#
#Funciones y operaciones básicas en Python

#Asociación de Variables
#type string
Estado = 'Sinaloa'
Localizacion = 'Noroeste'
Clima = 'Cálido, subhúmedo, seco, semiseco'
#Type int
SuperficieKM2 = int(57365)
PoblacionM = int(1532128)
PoblacionH = int(1494815)
#Type Float
Tpm_Anual_Cen = float(25.45)
Precipitacion_anual_mm = float(790.1)
PrcHabitantes_Culiacan = float(33.15)
PrcHabitantes_Mazatlan = float(16.57)

#Variables Adicionales
#1. La población total entre hombres y mujeres.
Total_HM = PoblacionH + PoblacionM
#2. El porcentaje total de la población entre Culiacán y Mazatlán.
Total_prcPoblacion = PrcHabitantes_Culiacan + PrcHabitantes_Mazatlan
#3. La temperatura media anual y los tipos de clima.
#--Descritos arriba (Durante el ejecicio)

print(
    '== Secretaría de Economía del estado de Sinaloa==' + '\n' + '\n'
    'Estado:' + Estado + '\n'
    'Localizacion:' + Localizacion + '\n'
    'Clima:' + Clima + '\n'
    'Superficie en Km2:' + str(SuperficieKM2) + '\n'
    'Temperatura Anual:' + str(Tpm_Anual_Cen) + '° \n'
    'Precipitacion Anual:' + str(Precipitacion_anual_mm) + 'mm \n' + '\n'
    'Poblacion' + '\n', 'Mujeres:' + str(PoblacionM) + '\n',
    'Hombres:' + str(PoblacionH) + '\n', 'Total:' + str(Total_HM) + '\n' + '\n'
    'Municipios con mayor porcentaje de habitantes:'
    '\n', 'Culiacan:' + str(PrcHabitantes_Culiacan) + '% \n',
    'Mazatlán:' + str(PrcHabitantes_Mazatlan) + '% \n',
    'Total:' + str(Total_prcPoblacion) + '% \n')

#Agustina Gpe. Arellanes Salazar
#21/06/2022 | 1800080037 | UPVE
