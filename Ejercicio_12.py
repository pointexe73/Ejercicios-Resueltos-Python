# Ejercicio 12: Imprimir el calendario para un año y mes especifico

import calendar

year = int(input("Write Year: "))
month = int(input("Write month: "))

print(calendar.month(year, month))