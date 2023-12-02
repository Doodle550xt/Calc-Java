import heapq
import time
class Grafo:

 def __init__(dijistra):
        dijistra.vertex = {}
        dijistra.edge = {}  
        dijistra.inicial = 0
        dijistra.final = 0
 def add_vertex(dijistra,vertice):
        if vertice not in dijistra.vertex:
            dijistra.vertex[vertice] = []
 def add_edge(dijistra, vertice_inicio, end_vertex, peso):
     if vertice_inicio in dijistra.vertex and end_vertex in dijistra.vertex:
         dijistra.edge[(vertice_inicio,end_vertex)] = peso
         dijistra.vertex[vertice_inicio].append(end_vertex)
         dijistra.vertex[end_vertex].append(vertice_inicio)
     else:
         print("Algun vertice no existe en el grafo")


 def __str__(dijistra):
     return f"Vertices: {dijistra.vertex}\n Aristas: {dijistra.edge}" 
 


 def dijkstra(dijistra, vertice_inicio):
    dijistra.inicial = time.time()
    distancias = {v: float('infinity') for v in dijistra.vertex}
    distancias[vertice_inicio] = 0

    lista = [(0, vertice_inicio)]

    while lista:
        distancia_actual, vertice_actual = heapq.heappop(lista)
        if distancia_actual > distancias[vertice_actual]:
            continue
        for vecinos in dijistra.vertex[vertice_actual]:

            peso = dijistra.edge.get((vertice_actual, vecinos), float('infinity'))
            peso_alrevez = dijistra.edge.get((vecinos, vertice_actual), float('infinity'))
            peso = min(peso, peso_alrevez)
            distance = distancia_actual + peso
            if distance < distancias[vecinos]:
                distancias[vecinos] = distance
                heapq.heappush(lista, (distance, vecinos))


    dijistra.final = time.time()
    return distancias
 
 def tiempo_tardado(dijistra):
     return (dijistra.final-dijistra.inicial)


 
 


vertice_inicio = 'A'
#GRAFO 1
grafo_1 = Grafo()

grafo_1.add_vertex('A')
grafo_1.add_vertex('B')

grafo_1.add_edge('A','B',2)

T1 = grafo_1.dijkstra(vertice_inicio)
TI_1 = grafo_1.tiempo_tardado()
print(f"GRAFO 1: Caminos mínimos desde {vertice_inicio}: {T1}")
print("Tiempo tardado: ",TI_1)

#GRAFO 2
grafo_2 = Grafo()

grafo_2.add_vertex('A')
grafo_2.add_vertex('B')
grafo_2.add_vertex('C')

grafo_2.add_edge('A','B',1)
grafo_2.add_edge('A','C',9)
grafo_2.add_edge('B','C',2)

T2 = grafo_2.dijkstra(vertice_inicio)
TI_2 = grafo_2.tiempo_tardado()
print(f"GRAFO 2: Caminos mínimos desde {vertice_inicio}: {T2}")
print("Tiempo tardado: ",TI_2)

#GRAFO 3
grafo_3 = Grafo()

grafo_3.add_vertex('A')
grafo_3.add_vertex('B')
grafo_3.add_vertex('C')
grafo_3.add_vertex('D')

grafo_3.add_edge('A','B',1)
grafo_3.add_edge('B','C',2)
grafo_3.add_edge('A','D',9)
grafo_3.add_edge('D','C',5)

T3 = grafo_3.dijkstra(vertice_inicio)
TI_3 = grafo_3.tiempo_tardado()
print(f"GRAFO 3: Caminos mínimos desde {vertice_inicio}: {T3}")
print("Tiempo tardado: ",TI_3)

#GRAFO 4
grafo_4 = Grafo()

grafo_4.add_vertex('A')
grafo_4.add_vertex('B')
grafo_4.add_vertex('C')
grafo_4.add_vertex('D')
grafo_4.add_vertex('F')

grafo_4.add_edge('B','C',2)
grafo_4.add_edge('C','F',6)
grafo_4.add_edge('F','D',5)
grafo_4.add_edge('D','B',3)
grafo_4.add_edge('A','C',4)
grafo_4.add_edge('A','D',1)



T4 = grafo_4.dijkstra(vertice_inicio)
TI_4 = grafo_4.tiempo_tardado()
print(f"GRAFO 4: Caminos mínimos desde {vertice_inicio}: {T4}")
print("Tiempo tardado: ",TI_4)

#GRAFO 5
grafo_5 = Grafo()

grafo_5.add_vertex('A')
grafo_5.add_vertex('B')
grafo_5.add_vertex('C')
grafo_5.add_vertex('D')
grafo_5.add_vertex('E')
grafo_5.add_vertex('F')

grafo_5.add_edge('A','B',1)
grafo_5.add_edge('B','C',2)
grafo_5.add_edge('C','D',3)
grafo_5.add_edge('D','E',4)
grafo_5.add_edge('E','F',5)
grafo_5.add_edge('A','F',6)
grafo_5.add_edge('F','C',7)
grafo_5.add_edge('E','C',8)
T5 = grafo_5.dijkstra(vertice_inicio)
TI_5 = grafo_5.tiempo_tardado()
print(f"GRAFO 5: Caminos mínimos desde {vertice_inicio}: {T5}")
print("Tiempo tardado: ",TI_5)
