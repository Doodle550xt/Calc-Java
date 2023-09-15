import time

def burbuja(n):
    arreglo = []
    for i in range(n):
        print(f"Ingresa el elemento {i+1} en el arreglo.")
        numero = int(input())
        arreglo.append(numero)
        
    inicio = time.time()
    for j in range(n):
        for k in range(n-1):
            if arreglo[k] > arreglo[k+1]:
                arreglo[k], arreglo[k+1] = arreglo[k+1], arreglo[k]
    fin = time.time()
    for h in range(n):
        print(arreglo[h])
        
    print("Tiempo de ejecución: {:.10f} segundos".format(fin - inicio))
    return arreglo

def Optimziadoburbuja(n):
    arreglo = []
    for i in range(n):
        print(f"Ingresa el elemento {i+1} en el arreglo.")
        numero = int(input())
        arreglo.append(numero)
        
    inicio = time.time()
    intercambio = True
    while intercambio:
        intercambio = False
        for j in range(n-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                intercambio = True
    fin = time.time()
    
    for h in range(n):
        print(arreglo[h])
        
    print("Tiempo de ejecución: {:.10f} segundos".format(fin - inicio))
    return arreglo

print("*          MENÚ         *")
print("*1.- Ordenar por burbuja*")
print("*2.- Burbuja optimizada *")

condicion = int(input("Ingresa tu elección: "))

if condicion == 1:
    print("Ingresa el tamaño del arreglo...")
    az = int(input())
    burbuja(az)
elif condicion == 2:
    print("Ingresa el tamaño del arreglo...")
    az = int(input())
    Optimziadoburbuja(az)
