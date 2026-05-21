def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x > y:
        return x
    else:
        return y

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    # Primero usamos nuestra función de arriba para saber cuál es el mayor entre x e y
    mayor_entre_dos = max_of_two(x, y)
    
    # Ahora comparamos ese resultado con el tercer número (z)
    if mayor_entre_dos > z:
        return mayor_entre_dos
    else:
        return z