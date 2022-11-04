Para generar un nuevo certificado es necesario ejecutar, desde la carpeta raiz

`python generador.py [nombre de la grafica]`

Por ejemplo

`python generador.py graficaA.txt`

El programa guardará el archivo como _certificadoN.txt_, donde _N_ corrresponde al nombre de la grafica

`ejemplares/certificadoA.txt`

La manera de ejecutar la práctica es 

`python main.py [nombre de la gráfica] [nombre del certificado]`

por ejemplo 

`python main.py graficaA.txt certificadoA2.txt`

Donde *A* hace referencia a la grafica y el 2 al certificado, otro ejemplo es

`python main.py graficaB.txt certificadoB1.txt`

**Advertencia:** La manera de abrir archivos en el programa con python es mediante la función open(ejemplares/archivo), el uso de la diagonal para especificar ruta puede variar según el sistema operativo, por lo general es barra / o barra invertida \.

