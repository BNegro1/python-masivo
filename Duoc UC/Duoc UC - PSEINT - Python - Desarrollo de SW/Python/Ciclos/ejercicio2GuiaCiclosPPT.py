# Ingrese por teclado 10 letras, 
# indique cuantas de ellas son vocales y cuántas son consonantes.

vocales = 'a, e, i, o, u'
consonates = 'b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z, ñ'
vo = 0
co = 0
for x in range(10):
    letra = input(f"Ingrese letra No.{x+1}: ")
    if letra in vocales:
        vo += 1
    elif letra in consonates:
        co += 1
print(f"Cantidad de vocales: {vo} | Cantidad de consonantes: {co}")