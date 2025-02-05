rutaArchivo = "/xml/ArchivoCalculos.txt"
unArchivo= open(rutaArchivo,'w')
unArchivo.write('Id: 3005, Fecha: 30/1/2022, EmisorNumero : 3101619800, Emisor:ASEGURADORA DEL ISTMO ADISA, Impuesto:296.36, Total:4700')
unArchivo.write('\nId: 3006, Fecha: 30/2/2022, EmisorNumero : 3101619800, Emisor:ASEGURADORA DEL ISTMO ADISA, Impuesto:296.36, Total:4700')
unArchivo.write('\nId: 3007, Fecha: 30/3/2022, EmisorNumero : 40158001, Emisor:JOSE FRANCISCO MORALES, Impuesto:296.36, Total:4700')
unArchivo.write('\nId: 3008, Fecha: 30/4/2022, EmisorNumero : 501180272, Emisor:BEATRIZ MILANES SEQUEIRA, Impuesto:296.36, Total:4700')
unArchivo.write('\nId: 3009, Fecha: 30/5/2022, EmisorNumero : 40158070, Emisor:MARIA ALEXANDRA M, Impuesto:296.36, Total:4700')
unArchivo.write('\nId: 3010, Fecha: 30/6/2022, EmisorNumero : 202510698, Emisor:JOSE PERAZA, Impuesto:296.36, Total:4700')
unArchivo.write('\nId: 3011, Fecha: 01/7/2022, EmisorNumero : 3101619800, Emisor:ASEGURADORA DEL ISTMO ADISA, Impuesto:296.36, Total:4700')

unArchivo.close

#ya tanemos el archivo en un arreglo tenemos un contador que empieze en cero

unArchivo = open(rutaArchivo,'r')
Lineas = unArchivo.readlines()
unArchivo.close()
Contador = 0
for linea in Lineas:
    print(linea)
    Contador += 1
    
archivo = open("archivo.txt", "r")
linea = archivo.readline()
print(linea)
#archivo = "/xml/ArchivoCalculos.txt"
while linea:
    linea = archivo.readline()
    print(linea)
    
archivo = open 

archivo = open("archivo.txt", "r")  # "r" indica modo lectura

