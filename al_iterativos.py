
def fiboo(n):

  resultado = [0,1]

  if (n>=2):
    for i in range (2,n+1):
     resultado.append(resultado[i-1]+resultado[i-2])
  return resultado[n]

def factorial(n):
  resultados = 1
  r = 1
  for j in range (1,n+1):
    r=r+1
    resultados = resultados*j
  return resultados


def printmenu():
 print("Ingresa la opción a utilizar:\n")
 print("1.- Fibonacci")
 print("2.- Factorial")
 print("3.- salir")
operador=0
while operador !=3:
  printmenu()
  operador = int(input("Ingresa la opción: "))
  if (operador==1):
   print("Ingresa la posición fibo")
   n = int(input())
   print(f"El fibonacci en la posición {n} es: {fiboo(n)}\n")
  elif (operador==2):
   print("Ingresa el numero a calcular factorial")
   n = int(input())
   print(f"{n}! es igual a {factorial(n)}\n")


