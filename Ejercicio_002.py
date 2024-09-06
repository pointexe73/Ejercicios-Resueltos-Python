# Ejercicio 2: Exponer el Uso Básico de la Función print

print("Este es un ejemplo")

# (END) Agrega un espacio al final de la línea o otro caracter especificado al final de linea
print("Este es otro ejemplo",end=" ")

print("de la funcion print",end=" ")

# Un print vacio da como resultado un saldo de linea
print()

print("Python","es","tremendo")

# (SEP) Agrega un separador entre los argumentos de la función print
print("Python","es","tremendo",sep="-")

print()

# Utilizando FORMAT para imprimir valores de variables en una cadena de texto
print('{} es {}'.format("Python","tremendo"))

print()

# Ejecurta una lista de numeros con f'strings
numeros = [1,2,3,4,5]
print(f'Los numeros son: {numeros}')

print()

# Ejecuta un diccionario f'strings
capitales = {"Colombia":"Bogota","Peru":"Lima"}
print(f'Las capitales de : {capitales}')

