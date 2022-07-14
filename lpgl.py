'''
Graficas por computador 2022
@author Luis Pedro Gonzalez Aldana
@author fualp
---Ambos soy yo----
Requerimientos:

Para poder optar a una nota distinta de cero, deben crear un escritor de imágenes BMP. Se debe de poder definir el tamaño de la ventana y se debe de poner un punto en cualquier lugar de la pantalla. Las imagenes deben poder abrirse en cualquier visor de imágenes que soporte BMP. No está permitido utilizar ninguna librería externa que no sea de las aprobadas por el profesors.

Pueden usar cualquier lenguaje de programación para realizar esto. Entregar código lógicamente similar al de sus compañeros de clase o a algún código disponible en internet resultará en una nota de 0 sin posibilidad de re-entrega. 

Las dudas sobre la manera de implementar cada uno de los puntos serán resueltas en clase. La tarea debe ser entregada en un zip con su nombre y número de carnet o con un link de GitHub.

Puntos:

Luego de cumplir con estos requerimientos, deben implementar estas features para obtener su nota. La nota máxima es 100.

(05 puntos) Deben crear una función glInit() que inicialice cualquier objeto interno que requiera su software renderer
(05 puntos) Deben crear una función glCreateWindow(width, height) que inicialice su framebuffer con un tamaño (la imagen resultante va a ser de este tamaño)
(10 puntos)  Deben crear una función glViewPort(x, y, width, height) que defina el área de la imagen sobre la que se va a poder dibujar (hint (Enlaces a un sitio externo.))
(20 puntos) Deben crear una función glClear() que llene el mapa de bits con un solo color
(10 puntos) Deben crear una función glClearColor(r, g, b) con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
(30 puntos) Deben crear una función glPoint(x, y) que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort.
glPoint(0, 0) cambia el color del punto en el centro del viewport, glPoint(1, 1) en la esquina superior derecha. glPoint(-1, -1) la esquina inferior izquierda.
(15 puntos) Deben crear una función glColor(r, g, b) con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.
(05 puntos) Deben crear una función glFinish() que escriba el archivo de imagen

'''

import struct #Esta libreria si la puedo

# Variables con bytes limitado
def char(c):
    #1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes
    return struct.pack('=h', w)

def dword(d):
    #4 bytes
    return struct.pack('=l', d)

def color(r, g, b):
    return bytes([int(b * 255),
                  int(g * 255),
                  int(r * 255)] )

class Renderer(object):
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.clearColor = color(0,0,0)
        self.currColor = color(1,1,1)

        self.glViewport(0,0,self.width, self.height)
        
        self.glClear()
