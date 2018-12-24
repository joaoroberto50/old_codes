def troca (s, novo, velho):
    aux = 0
    for c in s:
        if c == velho[aux] or c == velho[aux+1]:
            print(novo)
        else:
            print(c)
