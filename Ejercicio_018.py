# Ejercicio 18: Calcular la Suma de Tres Números e Incluir una Condición de Igualdad

def sumar_numeros(a, b, c):
    """
    Calcula la suma de tres numeros. Si los tres numeros son iguales.
    La suma se multiplica por 3.
    """
    suma = a + b + c
    
    if a == b and a == c:
        suma *= 3
    
    return suma

print(sumar_numeros(8, 4, 4))
print(sumar_numeros(2, 2, 2))