def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in text:
        if caracter in vocales:
            contador += 1
    return contador


def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contador = 0
    for caracter in text:
        if caracter in consonantes:
            contador += 1
    return contador


# --- ESTAS SON LAS FUNCIONES QUE TENÍAS QUE IMPLEMENTAR VOS ---

def total_letters(text):
    # Sumamos los resultados numéricos de las funciones de arriba
    return count_vowels(text) + count_consonants(text)


def vowel_percentage(text):
    total = total_letters(text)
    
    # Evitamos la división por cero si el texto no contiene letras (ej: "123")
    if total == 0:
        return 0.0
    
    # Calculamos el porcentaje y lo redondeamos a 1 solo decimal
    porcentaje = (count_vowels(text) / total) * 100
    return round(porcentaje, 1)


def analyze_text(text):
    vowels = count_vowels(text)
    consonants = count_consonants(text)
    total = total_letters(text)
    percentage = vowel_percentage(text)
    
    # Armamos la cadena final con el formato que los tests exigen
    return f"V:{vowels} C:{consonants} T:{total} P:{percentage}%"