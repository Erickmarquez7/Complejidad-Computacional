import numpy as np
import sys
from math import floor

###-------------------------LECTURA DEL ARCHIVO-------------------------------###
vertices = 0
aristas = 0
k = 0
primera_linea = ""
ultima_linea = ""
lista = []

archivo = sys.argv[1]

# Abrimos el archivo.
archivo = open('ejemplares/'+archivo)

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

print("El numero de vertices es " + str(vertices))
print("El numero de aristas es " + str(aristas))
print("El valor de K es " + str(k))
print("La representacion de nuestra matriz es:")
print(matriz)

###-------------------------LECTURA DEL CERTIFICADO-------------------------------###

# Nuestro certificado es una lista de conjuntos.
certificado = []
# Leemos el nombre del archivo que contiene el certificado
archivo_certificado = sys.argv[2]
# Abrimos el archivo.
archivo_certificado = open('ejemplares/'+archivo_certificado)


#Leemos el archivo caracter por caracter para poder crear nuestro certificado
while 1: 
    char = archivo_certificado.read(1)           
    if not char:  
        break  
    # Nos encontramos con el inicio del conjunto, así que podemos crear una instancia de éste
    if(char == '{'):
        s = set()  
    # Nos encontramos con un número, así que lo agregamos al conjunto
    if(char.isdigit()):
        s.add(int(char))      
    # Llegamos al final del conjunto, así que ya lo podemos agregar a la lista
    if(char == '}'):
        certificado.append(s)  
# archivo_certificado.close() 

print("El certificado: " + str(certificado))

###-------------------------------ALGORITMO------------------------------------###


#Primero rellamos la diagonal de la matriz con puros 1, tiempo cuadratico
for i in range(filas):
    for j in range(len(lista[i])):
        if i == j:
            matriz[i][j] = 1


#Suponemos como verdadera 
bandera = True

#Exploramos el certificado, en particular los conjuntos del certificado. Tiempo lineal
for k in certificado:
    filas = list(k)
    columnas = list(k)
    #print(filas, columnas)

    #exploramos la matriz. Tiempo cuadratico
    for i in filas:
        for j in columnas:
            if matriz[i-1][j-1] == 0:
                bandera = False
    #total: cubico
        
if bandera == True:
    print('El ejemplar con el certificado dado satisface la condición')
    print('de pertenencia al lenguaje')
else:
    print('El ejemplar con el certificado dado NO satisface la condición')
    print('de pertenencia al lenguaje')

