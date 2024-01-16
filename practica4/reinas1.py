
#ESTRATEGIA 1: Técnica de poda 

def is_valid(row,cols,reinas):
    for r in range(row):
        if cols ==  reinas[r] or abs(cols-reinas[r]) == abs(row - r): # en esta condición implementamos ambos casos en un solo IF, reduciendo las exploreaciones inecesarias para ambos casos
            return False
       
    return True
        
def place_reinas(row,reinas,n):
    if row == n:
        print(reinas)
        return 1
    else:
        total_sols = 0
        for cols in range(n):
            if is_valid(row,cols,reinas):
                reinas[row] = cols
                total_sols += place_reinas(row+1,reinas,n)
        return total_sols

def n_reinas_poda(n):
    reinas = [""]*n
    row = 0
    return place_reinas(row,reinas,n)


