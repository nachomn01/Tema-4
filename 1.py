# Desarrollar los algoritmos necesarios para generar un árbol de Huffman a partir de la siguiente tabla
# –para lo cual deberá calcular primero las frecuencias de cada carácter a partir de la cantidad de
# apariciones del mismo–, para resolver las siguientes actividades:
# a. la generación del árbol debe hacerse desde los caracteres de menor frecuencia hasta los de mayor,
# en el caso de que dos caracteres tengan la misma frecuencia, primero se toma el que este primero en
# el alfabeto, el carácter “espacio” y “coma” se consideraran anteúltimo y último respectivamente en
# el orden alfabético;

# b. descomprimir los siguientes mensajes –cuyo árbol ha sido construido de la misma manera que el
# ejemplo visto anteriormente:

# I. Mensaje 1: “100010111010110000101110100011100000110110000001111001111010010110
# 0001101001110011010001011101011111110100001111001111110011110100011000110000
# 00101101011110111111101110101101101110011101101111001111111001010010100101000001
# 011010110001011001101000111001001011000011001000110101101010111111111110110111
# 0111001000010010101100011111110001000111011001100101101000110111110101101000
# 1101110000000111001001010100011111100001100101101011100110011110100011000110
# 000001011010111110011100”

mensaje1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"

# II. Mensaje 2:
# “01101010110111001010001111010111001101110101101101000010001110101001
# 011110100111111101110010100011110101110011011101011000011000100110100011100100
# 10001100010110011001110010010000111101111010”

# c. finalmente, calcule el espacio de memoria requerido por el mensaje original y el comprimido.

import numpy as np 
import math
import heapq
import sys

class Nodo:
    def __init__(self,caracter,frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self .izquierda = None
        self.derecha = None
        self.codigo = ''
    
    def __lt__(self,other):
        return self.frecuencia < other.frecuencia

    def __eq__(self,other):
        if (other == None):
            return False
        if (not isinstance(other,Nodo)):
            return False
        return self.frecuencia == other.frecuencia
 
def generar_arbol(caracteres, frecuencias):
    heap = []
    for i in range(len(caracteres)):
        heapq.heappush(heap, Nodo(caracteres[i],frecuencias[i]))

    while (len(heap) > 1):
        nodo_izquierdo = heapq.heappop(heap)
        nodo_derecho = heapq.heappop(heap)
        frecuencia_sumada = nodo_izquierdo.frecuencia + nodo_derecho.frecuencia
        nuevo_nodo = Nodo(None,frecuencia_sumada)
        nuevo_nodo.izquierda = nodo_izquierdo
        nuevo_nodo.derecha = nodo_derecho
        heapq.heappush (heap, nuevo_nodo)
    
    return heap[0]

def generar_codigo(raiz, codigo_actual, codigos):
    """ Guarda en las hojas la secuencia de bits que van desde la raíz a cada hoja y genera un diccionario, 
    """
    if (raiz == None):
        return 
    # Las hojas tienen caracter 
    if (raiz.caracter != None):
        codigos[raiz.caracter] = codigo_actual
        raiz.codigo = codigo_actual
        return
    
    # Los nodos intermedios no tienen caracter
    generar_codigo(raiz.izquierda,codigo_actual + "0", codigos)
    generar_codigo(raiz.derecha, codigo_actual + "1", codigos)

def codificar (mensaje, codigos):
    """ Codifica el mensaje basado en el diccionario de codigos
    Mensaje str: Cadena de caracteres
    """
    codigo = ''
    for caracter in mensaje:
        codigo += codigos[caracter]
    return codigo

def decodificar (raiz, indice, codigo):
    """ Decodifica una cadena de bits de un caracter 
    raiz : Nodo
    indice : bit 
    """

