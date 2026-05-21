def number_to_month(month):
    # Dejamos "error" en la posición 0. 
    # Así, enero queda en la 1, febrero en la 2... y abril en la 4.
    meses = ["error", "enero", "febrero", "marzo", "abril", "mayo", "junio", 
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    # Validamos estrictamente que el número esté entre 1 y 12 inclusive
    if 1 <= month <= 12:
        return meses[month]
    else:
        return "error"