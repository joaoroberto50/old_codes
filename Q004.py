def troca(s, velho, novo):
    b = ''
    aux = ''
    x = ''
    z = len(velho)
    a = z
    y = len(novo)
    d = y
    for c in s:
        if c == velho[(z-a)]:
            aux = aux + novo[y-d]
            b += c
            z+=1
            if z-a>= a:
                z = a
            y+=1
            if y-d >= d:
                y = d
            if len(aux) == z:
                x+=aux
                b = ''
        else:
            x += b+c
            aux = ''
            b = ''
            z = len(velho)
            y = len(novo)
    print(x)
