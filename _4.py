# Ejercicio 4: Solicitar el Valor del Radio de un Círculo para Calcular su Área
# Se importo el valor de pi de la libreria math para realizar el calculo del area del circulo
from math import pi

radio = float(input("Ingrese el valor del radio del círculo: "))
# pi es multiplicado por radio y elevado al cuadrado para calcular el area del circulo
area = pi * radio ** 2
# Imprime el area del circulo
print(f'El area de un circulo es: {area}')
