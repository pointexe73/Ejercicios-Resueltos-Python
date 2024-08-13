# Ejercicio 3: Obtener la Fecha y Hora Actuales del Sistema con el Módulo datetime
# Se importa el modulo datetime para obtener infomacion sobre fecha y hora actuales del sistema
import datetime 
# Se utiliza la funcion datetime.datetime.now() para obtener la fecha y hora actuales del sistema
Time = datetime.datetime.now()
# Se imprime la fecha y hora actuales del sistema en el formato deseado utilizando la funcion strftime()
print(Time.strftime('%d/%m/%Y %H:%M:%S'))