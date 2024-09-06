# Ejercicio 14: Calcular la Diferencia en Días de Dos Fechas Dadas

# Importa la función 'date' del módulo 'datetime'
from datetime import date 

# Define la fecha actual
hoy = date(2019, 9, 16)

# Define una fecha diferente
otra_fecha = date(2023, 2, 13)

# Calcula la diferencia entre las dos fechas
delta = otra_fecha - hoy 

# Imprime el resultado de la diferencia como un objeto 'timedelta'
print(delta)

# Imprime el número de días en la diferencia
print(delta.days)