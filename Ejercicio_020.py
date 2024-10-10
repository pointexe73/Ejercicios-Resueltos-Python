# Ejercicio 20: Emular el Funcionamiento del Producto de Cadenas de Caracteres

def producto_cadena(cadena, repeticion):
    """
    Emula el funcionamiento del producto (*)de cadenas 
    """
    resultado = ""
    
    # Itera 'repeticion' veces, concatenando 'cadena' a 'resultado' en cada iteración
    for i in range(repeticion):
        resultado += cadena
    # Retorna el resultado final, que es la cadena original repetida 'repeticion' veces
    return resultado

print(producto_cadena("Hola", 3))
