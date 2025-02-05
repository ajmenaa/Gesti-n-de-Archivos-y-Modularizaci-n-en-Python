# estadisticas.py
# estadisticas.py
def media(datos):
    """esta funcion calcula la media aritmetica de una lista con valores numericos

    Args:
        datos (_type_): Lista de numeros

    Returns:
        _type_: Flotante de la media aritmetica de una lista
    """    
    return sum(datos) / len(datos)

def calcular_mediana(datos):

    datos_sorted = sorted(datos)
    n = len(datos)
    mid = n // 2
    if n % 2 == 0:
        return (datos_sorted[mid - 1] + datos_sorted[mid]) / 2.0
    else:
        return datos_sorted[mid]