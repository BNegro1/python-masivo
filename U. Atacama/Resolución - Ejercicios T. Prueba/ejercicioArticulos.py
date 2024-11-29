def procesar_articulo(tipo, categoria, nombre, precio, dias_restantes):
    if tipo == "navidad":
        if dias_restantes > 50:
            ubicacion = "bodega"
        elif dias_restantes > 30:
            ubicacion = "gondola"
            precio = precio * 0.5 # 50% de descuento en Halloween
        elif dias_restantes > 15:
            ubicacion = "isla"
            if categoria == "regalos" or categoria == "juguetes":
                precio = precio * 0.85 # 15% de descuento en regalos y juguetes
            elif categoria == "otros":
                precio = precio * 0.8 # 20% de descuento en otros
        else:
            if categoria == "luces" or categoria == "adornos" or categoria == "arboles":
                ubicacion = "remate"
                precio = precio * 0.5 # 50% de descuento en luces, adornos y arboles
            elif categoria == "regalos" or categoria == "juguetes":
                ubicacion = "isla"
                precio = precio * 0.85 # 15% de descuento en regalos y juguetes
            else:
                ubicacion = "gondola"
                precio = precio * 0.8 # 20% de descuento en otros
    else: # tipo == "halloween"
        if dias_restantes > 50:
            ubicacion = "gondola"
        else:
            ubicacion = "bodega"
            
    return ubicacion, precio
