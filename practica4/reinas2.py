
#ESTRATEGIA 2: Heuristicas

def is_valid(row, col, reinas):
    for r in range(row):
        if col ==  reinas[r] or abs(col-reinas[r]) == abs(row - r): # en esta condición implementamos ambos casos en un solo IF, reduciendo las exploreaciones inecesarias para ambos casos
            return False
    return True

def get_remaining_values(row, reinas, n):
    valid_cols = [col for col in range(n) if is_valid(row, col, reinas)]
    return sorted(valid_cols, key=lambda x: sum(1 for r in range(row + 1, n) if is_valid(r, x, reinas)))

def place_reinas(row, reinas, n):
    if row == n:
        print(reinas)
        return 1
    else:
        total_sols = 0
        remaining_values = get_remaining_values(row, reinas, n)
        for col in remaining_values:
            reinas[row] = col
            total_sols += place_reinas(row + 1, reinas, n)
        return total_sols

def n_reinas_heuristica(n):
    reinas = [0]*n
    row = 0
    return place_reinas(row,reinas,n)


