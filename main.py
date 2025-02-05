# Proyecto: [Nombre del Proyecto]
# Estudiante: JOSE FRANCISCO MORALES MILANES
# Fecha de Inicio: 2025/02/24
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

# from analisis_datos.estadisticas import media,calcular_mediana
from analisis_datos import *

#para debbugear le damos un break point y luego le damos f11

lista_compras = generar_lista_de_compras()
print(lista_compras)


lista_parametro = [5,3,1,2,4]
print('Media:', media(lista_parametro) )
print('Mediana:', calcular_mediana(lista_parametro))

precios = [precio for _, precio in lista_compras]
print('Media:', media(precios) )
print('Mediana:', calcular_mediana(precios))