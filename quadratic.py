import math

def value_y(a, b, c, x):
    # Calcula el valor de Y para un X dado
    return (a * (x ** 2)) + (b * x) + c


def roots(a, b, c):
    # Calculamos el discriminante (lo que va adentro de la raíz: b^2 - 4ac)
    discriminante = (b ** 2) - (4 * a * c)
    
    # Caso 1: Dos raíces reales (discriminante positivo)
    if discriminante > 0:
        r1 = (-b + math.sqrt(discriminante)) / (2 * a)
        r2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"({r1}, {r2})"
    
    # Caso 2: Una sola raíz (discriminante igual a cero)
    elif discriminante == 0:
        r12 = -b / (2 * a)
        return f"({r12})"
    
    # Caso 3: Ninguna raíz real (discriminante negativo)
    else:
        return "( )"


def to_string(a, b, c):
    # Evaluamos los 4 casos específicos que pide el test de la consigna
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):
    # La derivada de a*X^2 + b*X + c es siempre: (2*a)*X + b
    # Evaluamos cómo mostrar el texto según los casos del test
    if a == 0 and b == 0:
        return "f'(x) = 0"
    elif a == 0:
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {2 * a} * X"
    else:
        return f"f'(x) = {2 * a} * X + {b}"