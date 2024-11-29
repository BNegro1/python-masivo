vocales = 'a, e, i, o, u'
consonates = 'b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z, ñ'
vo = 0
co = 0
letra = input(f"Ingrese frase: ")
for x in letra:
    if x in vocales:
        vo += 1
    elif x in consonates:
        co += 1
print(f"Cantidad de vocales: {vo} | Cantidad de consonantes: {co}")