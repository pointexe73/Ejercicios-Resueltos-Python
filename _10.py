# Ejercicio 10: Solicitar al Usuario un Numero n y Calcular n + nn + nnn

# n = 3 -> 3 + 33 + 333 = 369

# Solicitar al usuario que introduzca un número
n = input("Introduce un número n: ")

# Convertir el número a cadena y duplicarlo para obtener nn
nn = int('{}{}'.format(n, n))

# Convertir el número a cadena y triplicarlo para obtener nnn
nnn = int('%s%s%s' % (n, n, n))

# Convertir el número n a entero
n = int(n)

# Calcular la suma de n + nn + nnn
suma = n + nn + nnn

# Imprimir la suma
print(suma)