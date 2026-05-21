# --- ESTAS FUNCIONES YA VIENEN EN EL ARCHIVO (NO LAS TOQUES) ---
def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0

def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0


# --- ESTA ES LA FUNCIÓN QUE TENÉS QUE IMPLEMENTAR VOS ---
def classify_number(n):
    # 1. Caso especial: si es cero, devolvemos "zero" al toque
    if n == 0:
        return "zero"
    
    # 2. Evaluamos los casos para números positivos
    elif is_positive(n):
        if is_even(n):
            return "positive even"
        else:
            return "positive odd"
            
    # 3. Si no es cero ni es positivo, por descarte es un número negativo
    else:
        if is_even(n):
            return "negative even"
        else:
            return "negative odd"