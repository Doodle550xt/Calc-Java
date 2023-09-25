
def factorial(n):
    
    if (n==0 or n==1):
        resultado = 1
       # print(resultado) 
    elif n > 1:
        resultado = n * factorial(n-1)
    return resultado

def fibonacci(n):
    if (n==0):
        resultado = 0
    elif n==1:
        resultado = 1
    elif n>1:
        resultado = fibonacci(n-2)+fibonacci(n-1)
    return resultado

print("ingresa un número para calcular factorial: ")
n = int(input())
print("ingresa un número para calcular fibonacci: ")
resultado1  = factorial(n)
x = int(input())
resultado2 = fibonacci(x)

print(f"El factorial de {n} es {resultado1}")
print(f"El fibonacci en posición {x} es {resultado2}")
    
