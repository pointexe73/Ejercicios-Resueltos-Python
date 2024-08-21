# Ejercicio 5: Obtener la Representación Inversa de una Cadena de Caracteres

# Forma 1
cadena = "python"
print(cadena[::-1])

# Forma 2

cadena = "python"
# range(len(cadena) -1, -1, -1) Genera una secuencia de números desde 5 hasta -1, con un paso de -1
for i in range(len(cadena) -1, -1, -1):
    print(cadena[i], end="")
    