# Ejercicio 7: Obtener el Nombre de Extensión de un Nombre de Archivo

# Escribe el nombre completo con la extencion del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Ejemplo (main.py)
# SPLIT() -> ['main', 'py'] Separa cada "." en una lista
partes_nombre_archivo = nombre_archivo.split(".")

print(partes_nombre_archivo)

# Con -1 obtenemos el ultimo elemento de la lista
print("La extensión del archivo es:", partes_nombre_archivo[-1])

# Otra forma que obtener el mismo resultado
print(f'La extencion del archivo es: {nombre_archivo[-2:]}')