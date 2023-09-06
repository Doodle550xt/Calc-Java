numero1 = int(input("Introduzca el primer número\n"))
numero2 = int(input("Introduzca el segundo número\n"))

condicion = 0

while condicion!= 6:
  print("""
  Ingresa el operador a utilizar
  1. +
  2. -
  3. *
  4. /
  5. CAMBIAR NÚMEROS
  6. SALIR
  """) 
  condicion = int(input())
  if condicion == 1:
    print("El resultado es de: ", numero1+numero2)
  elif condicion == 2:
    print("El resultado es de: ", numero1-numero2)
  elif condicion == 3:
    print("El resultado es de: ", numero1*numero2)
  elif condicion == 5:
    numero1 = int(input("Introduzca el primer número\n"))
    numero2 = int(input("Introduzca el segundo número\n"))
  elif condicion == 4:
    if numero2 ==0:
      print("No se puede dividir entre 0 \n")
    else:
      print("El resultado es de: ", numero1/numero2)
  
  
     
  
  