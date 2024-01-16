#ORIGINAL

def is_valid(row,cols,reinas):
    for r in range(row):
        if cols ==  reinas[r]:
            return False
        elif abs(cols-reinas[r]) == abs(row - r):
            return False
    return True
        



def place_reinas(row,reinas,n):
    if row == n:
        print(reinas)
        return 1
    else:
        total_sols = 0
        for cols in range(n):
            #print(reinas)
            if is_valid(row,cols,reinas):
              #  print("Posición:",cols," fué válida")
                reinas[row] = cols
                total_sols += place_reinas(row+1,reinas,n)
          #  else:
                # print("Posición:",cols," no fué válida")
        return total_sols



def n_reinas(n):
    reinas = [""]*n
    row = 0
    return place_reinas(row,reinas,n)




