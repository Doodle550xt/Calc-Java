import time
numeros = [32, 39, 133, 47, 46, 161, 134, 14, 68, 167, 21, 2, 140, 148, 116, 153, 4, 104, 30, 101, 135, 197, 43, 154, 183, 188, 155, 192, 110, 145, 164, 172, 62, 102, 41, 96, 72, 114, 156, 77, 136, 35, 141, 152, 107, 117, 56, 139, 94, 196, 74, 198, 71, 45, 112, 88, 162, 185, 53, 106, 3, 76, 159, 51, 79, 149, 59, 17, 22, 187, 123, 165, 179, 60, 80, 122, 5, 15, 126, 87, 115, 189, 97, 194, 109, 61, 23, 12, 44, 166, 91, 103, 36, 138, 130, 8, 174, 175, 63, 95, 127, 157, 119, 177, 180, 158, 151, 52, 105, 34, 131, 31, 200, 150, 6, 132, 28, 16, 195, 93, 99, 66, 7, 33, 67, 42, 9, 86, 111, 37, 169, 170, 199, 50, 1, 29, 176, 143, 146, 113, 70, 38, 98, 82, 55, 168, 64, 118, 144, 24, 128, 25, 78, 75, 163, 84, 137, 100, 54, 160, 18, 81, 49, 73, 121, 90, 171, 48, 108, 193, 27, 20, 190, 10, 69, 120, 19, 186, 26, 57, 92, 142, 58, 40, 65, 173, 129, 147, 184, 191, 83, 178, 182, 124, 11, 181, 85, 13, 125, 89]

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
