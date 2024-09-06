# Python - Ejercicio 15: Calcular el Volumen de una Esfera a partir del Radio Dado

# Importamos la funcion pi del modulo math
from math import pi

# Usuario ingresa un numero
r = float(input('Escriba el radio de la esfera: '))

# Formula para calcular el radio de una esfera
volumen = 4/3 * pi * r ** 3

# Imprime el resultado
print(f'El volumen de la esfera es {volumen} unidades cubicas')