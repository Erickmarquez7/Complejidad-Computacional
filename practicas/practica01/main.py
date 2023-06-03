import numpy as np
import sys
from math import floor

#LECTURA DEL ARCHIVO
vertices = 0
aristas = 0
k = 0
primera_linea = ""
ultima_linea = ""
lista = []

archivo = sys.argv[1]

# Abrimos el archivo.
archivo = open(archivo)

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

#-------------------------------------------------------------
#Solución al problema 

class Vertice:
    '''Clase auxiliar de vurtices que nos ayudara a encontrar determinar
    los vecinos de un vértice así como si el color del vertice'''
    def __init__(self, id, vecinos):
        self.id = id
        self.vecinos = vecinos
        self.color = 0 #quiere decir que el vértice no ha sido coloreado
    
    def get_vecinos(self):
        return self.vecinos
    
    def get_id(self):
        return self.id

    
    def __str__(self):
        return f'({self.id})'

    def __repr__(self):
        return f'({self.id})'



def complemento(matriz):
    '''Obtiene el complemento de la grafica representado por una matriz'''
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == 1:
                matriz[i][j] = 0
            elif matriz[i][j] == 0:
                matriz[i][j] = 1
            if i == j:
                matriz[i][j] = 0
    return matriz


def convert_to_adjacency(matrix):
    '''Convierte la matriz de adyacencias en una lista de adyacencias
    donde el indice i la lista nos indica a que vertices es adyacente
    el vertice i'''
    start = 0
    res = []
    lst = []
    n = len(matrix)

    for i in range(n):
        res.append(lst*n)
    while start < n:
        y = matrix[start]
        for i in range(len(y)):
            if y[i] == 1:
                res[start].append(i)
        start += 1
    return res


def convierte(lista):
    '''Convierte la lista de adyacencias de tipo int a una 
    lista de adyacencias de tipo vertice'''
    vertices = []
    i=0
    for adyacencias_nodo in lista:
        nodo_aux = Vertice(i, adyacencias_nodo)
        vertices.append(nodo_aux)
        i+=1
    return vertices


def colorea(vertice):
    '''Empieza la coloracion de vértices a partir del vértice dado'''
    vertice.color = 1 #coloreamos con el primer color
    if explora(vertice) == True:
        return True
    else:
        return False

def explora(verticew):
    vecinos = verticew.get_vecinos()
    for vecx in vecinos:
        vecx = lista_vert[vecx]
        if vecx.color == verticew.color: #si tiene la misma coloracion entonces falso
            return False
        else:
            if vecx.color == 0: #si el vértice aun no es coloreado
                if verticew.color == 1: #si tiene color de 1
                    vecx.color = 2 #lo coloreamos con el otro
                    explora(vecx) #recursión sobre los vecinos del vecino
                else:
                    vecx.color = 1 #lo coloreamos con el color 1
                    explora(vecx)
    return True #en algún momento todos estan coloreados, por lo que podemos regresar True


print('Aplicacion del algoritmo')
#primero convertimos la matriz a su complemento
matriz_c = complemento(matriz)
#convertimos el complemento en una lista de adyacencias
lista_int = convert_to_adjacency(matriz_c)

#el problema es que son numeros, y nosotros queremos vertices
#lo convertimos en lista de vertices
lista_vert = convierte(lista_int)


#exploramos
valor = colorea(lista_vert[0])

clan1=[]
clan2=[]

if valor:
    for vertice in lista_vert:
        if vertice.color == 1:
            clan1.append(vertice.get_id()+1) #Este mas uno es solo par que coincida
        else:                                #con el id del dibujo del grafo
            clan2.append(vertice.get_id()+1) #ya que el algoritmo trabaja con indices empezando
                                             #desde 0, y en la grafica empezamos desde 1
    print('Clan 1:', clan1)
    print('Clan 2:', clan2)

else:
    print('No contiene dos clanes')