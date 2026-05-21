# --- ESTAS FUNCIONES YA VIENEN EN EL ARCHIVO (NO LAS TOQUES) ---
def apply_discount(price, discount_pct):
    """Dado un precio y un porcentaje de descuento, retorna el precio con el descuento aplicado."""
    return price * (1 - discount_pct / 100)

def apply_tax(price, tax_pct):
    """Dado un precio y un porcentaje de impuesto, retorna el precio con el impuesto aplicado."""
    return price * (1 + tax_pct / 100)


# --- ESTAS SON LAS FUNCIONES QUE TENÉS QUE IMPLEMENTAR VOS ---

def final_price(price, quantity, discount_pct, tax_pct):
    # 1. Calculamos el subtotal de la compra
    subtotal = price * quantity
    
    # 2. Le aplicamos el descuento al subtotal
    con_descuento = apply_discount(subtotal, discount_pct)
    
    # 3. Al precio descontado le sumamos el impuesto
    con_impuesto = apply_tax(con_descuento, tax_pct)
    
    # 4. Redondeamos a 2 decimales y lo devolvemos
    return round(con_impuesto, 2)


def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    # Calculamos el precio final de la opción A usando nuestra función de arriba
    total_a = final_price(price_a, qty_a, disc_a, tax_pct)
    
    # Calculamos el precio final de la opción B de la misma manera
    total_b = final_price(price_b, qty_b, disc_b, tax_pct)
    
    # Comparamos cuál conviene más. Si el precio de A es menor o igual, gana A
    if total_a <= total_b:
        return "A"
    else:
        return "B"