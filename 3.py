# Se requiere implementar una red de ferrocarriles compuesta de estaciones de trenes y cambios de
# agujas (o desvíos). Contemplar las siguientes consideraciones:
#           a. cada vértice del grafo no dirigido tendrá un tipo (estación o desvió) y su nombre,
#              en el caso de los desvíos el nombre es un número –estos estarán numerados de manera consecutiva–;
#           b. cada desvío puede tener múltiples puntos de entrada y salida;
#           c. se deben cargar seis estaciones de trenes y doce cambios de agujas;
#           d. cada cambio de aguja debe tener al menos cuatro salida o vértices adyacentes;
#           e. y cada estación como máximo dos salidas o llegadas y no puede haber dos estaciones conectadas directamente;
#           f. encontrar el camino más corto desde:
#               1). la estación King's Cross hasta la estación Waterloo,
#               2). la estación Victoria Train Station hasta la estación Liverpool Street Station,
#               3). la estación St. Pancras hasta la estación King's Cross;

import sys 
import math 
import heapq

class GrafoNoDirigido:
    def __init__(self):
        # Diccionario vertice: lista de tuplas (vertices,peso)
        self.vertices = {}
        self.cantidad_vertices = 0

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
            self.cantidad_vertices += 1
    
    def agregar_arista (self, vertice1, vertice2, peso):
        self.agregar_vertice(vertice1)
        self.agregar_vertice(vertice2)
        self.vertices[vertice1].append((vertice2,peso))
        self.vertices[vertice2].append((vertice1,peso))

    def cargar_desde_archivo(self, archivo):
        with open(archivo) as f:
            for linea in f:
                vertice1, vertice2, peso = linea.strip().split(',')
                self.agregar_arista(vertice1, vertice2, int(peso))
    
    def obtener_vertices(self):
        return self.vertices.keys()

    
#Buscar camino de grafo no dirigido

grafo = GrafoNoDirigido()

estacionA = grafo.agregar_vertice("A")
estacionB = grafo.agregar_vertice("B")
estacionC = grafo.agregar_vertice("C")
estacionD = grafo.agregar_vertice("D")
estacionE = grafo.agregar_vertice("E")
estacionF = grafo.agregar_vertice("F")


grafo.agregar_arista(estacionA,estacionB,2)
grafo.agregar_arista(estacionA,estacionC,4)
grafo.agregar_arista(estacionA,estacionF,3)
grafo.agregar_arista(estacionA,estacionD,1)


