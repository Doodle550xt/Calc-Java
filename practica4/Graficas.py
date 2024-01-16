import reinas,reinas1,reinas2
import time
import matplotlib.pyplot  as plt
tablero = 4
start1 = time.time()
print(reinas.n_reinas(tablero))
end1 = time.time()
print(reinas1.n_reinas_poda(tablero))
end2 = time.time()
print(reinas2.n_reinas_heuristica(tablero))
end3 = time.time()

print("Tiempo normal:",end1-start1)
print("Tiempo de poda:",end2-end1)
print("Tiempo de heuristica:",end3-end2)

tiempos = [end1-start1,end2-end1,end3-end2]
#tiempos = [1,2,3]
mediciones = ["Normal","Poda","Heuristica"]
plt.bar(mediciones,tiempos,color =["blue","red","green"])
plt.xlabel("mediciones")
plt.ylabel("Tiempo")
plt.title("N-REINAS")
plt.show()
