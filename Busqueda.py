import time

arreglo = []
#Ordenar optimizado
def Optimziadoburbuja(n):
  intercambio  = bool(True)
  while intercambio==True:
   intercambio = False
   for j in range(n):
     for k in range(n-1):
      if arreglo[k]>arreglo[k+1]:
         temp = arreglo[k]
         arreglo[k] = arreglo[k+1]
         arreglo[k+1] = temp
         intercambio = True

  return 1

#busqueda binaria
def binarial(n):
  Optimziadoburbuja(len(arreglo))
  #empieza busqueda bianria
  inicio = 0
  fin = len(arreglo)-1
  
  for i in range (fin):
   center = (inicio+fin)//2
   #si el numero que estoy buscando es menor que el centro entonces:
   if n==arreglo[center]:
     print("Se encontró en la posición del medio")
     return 1
   if arreglo[center]<n:
     inicio = center+1
   else:
     fin = center-1
  print("No se encontró")  
  return 0

     


#lineaal
def lineal(b):
 i = 0
 position = 0
 flag = False
 while ((i<len(arreglo)) and flag ==False):
  if (arreglo[i]==b):
   flag = True
   position = i 
  i=i+1
  if (flag==True):
    print("Se encontró el dato en el arreglo en la posición [" + str(position+1) +"]")
    return 1
  
 print("No se encontró el dato en el arreglo")

#definicion de arreglos
def arreglos(n):
  
 
   for i in range (n):
    print(f"Ingresa el elemento {[i+1]}: en el  arreglo.")
    numeros = int(input())
    arreglo.append(numeros)
    #termina de pedir datos para llenar el arreglo
  

  

print("Ingresa el tamaño del arreglo...")
az = int(input())
arreglos(az)
print("*          MENÚ         *\n")
print("*1.- Busqueda lineal    *\n")
print("*2.- Busqueda binaria   *\n")
print("*3.- Busqueda Salir   *\n")
condicion = int(input())
if (condicion == 1):
  inicio = time.time()
  print("Ingresa el número a buscar")
  search = int(input())
  lineal(search)
  
  fin = time.time()
elif (condicion==2):
   inicio = time.time()
   print("Ingresa el número a buscar")
   search = int(input())
   binarial(search)

   fin = time.time()
print(f"Tiempo de ejecución: {fin - inicio} segundos")
