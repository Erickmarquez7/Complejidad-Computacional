import numpy as np
import sys
from math import floor, ceil
import random

###--------------------LECTURA DEL ARCHIVO DE LA GRAFICA-------------------------###
vertices = 0
aristas = 0
k = 0
primera_linea = ""
ultima_linea = ""
lista = []

archivor = sys.argv[1]

# Abrimos el archivo.
archivo = open('ejemplares/'+archivor)

# La linea 1 contiene el número k en binario
k = int(archivo.readline().strip('\n'), 2)

# Pasamos a la siguiente linea
linea = next(archivo)

# Leemos el archivo a partir de la tercera linea (que es donde esta la matriz)
# y le quitamos todos los saltos de línea
for linea in archivo:
    lista.append(linea.strip('\n'))

# Creamos la matriz
filas = len(lista)
matriz = np.zeros((filas, filas), dtype=int)

# Obtenemos el número de vertices
vertices = filas

# Rellenar la matriz con lo leido del fichero
for i in range(filas):
    for j in range(len(lista[i])):
        matriz[i,j] = lista[i][j]

for i in range(filas):
    for j in range(len(lista[i])):
        if matriz[i,j] == 1:
            aristas = aristas + 1

# La matriz es simétrica, así que como estamos contando todas las posibles 
# aristas, hay que dividir ese número entre dos. 
aristas = floor(aristas/2)

###-------------------------GENERADOR DEL CERTIFICADO-------------------------------###
elementos = list(range(1,vertices+1))
valores = ["floor", "ceil"]
#eleccion aleatoria
valor = random.choice(valores)
certificado = "["
cc = 0
repeticion = len(elementos)

while(k != 0):
    if(valor == 'floor'):
        cc = floor(len(elementos)/k)
    else:
        cc = ceil(len(elementos)/k)
        
    certificado += "{"
    
    while(cc != 0):
        elemento_random = random.choices(elementos).pop()
        certificado += str(elemento_random)
        elementos.remove(elemento_random)
        if(cc != 1):
            certificado += ","
            
        cc -= 1
        
    certificado += "},"
    k -= 1


certificado = certificado[:-1]+"]"

# Guardamos el certificado en ejemplares/certificadoA.txt
nombre = archivor[7]
#lo guardamos con el nombre del arvhivo
f = open('ejemplares/certificado'+nombre+'.txt', 'w')
f.write(certificado)
f.close