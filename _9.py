# Ejercicio 9: Mostrar la Fecha de un Evento Almacenada en una Tupla

# Define una tupla que almacena la fecha del evento
fecha_evento = (2023, 9, 14)

# Imprime el tipo de dato de la variable fecha_evento
print(type(fecha_evento))

# Imprime la tupla completa
print(fecha_evento)

# Imprime un mensaje con la fecha del evento utilizando la tupla directamente
print('El evento progamado sera para la fecha:', fecha_evento)

# Imprime un mensaje con la fecha del evento utilizando la formatación de cadenas con %
print('El evento progamado sera para la fecha: %i/%i/%i' % fecha_evento)

# Desempaqueta los elementos de la tupla en variables individuales
year, month, day = fecha_evento

# Imprime un mensaje con la fecha del evento utilizando la formatación de cadenas con format()
print('El evento sera el {}/{}/{}'.format(day, month, year))

# Imprime un mensaje con la fecha del evento utilizando f-strings
print(f"El evento sera el {fecha_evento[2]}/{fecha_evento[1]}/{fecha_evento[0]}")