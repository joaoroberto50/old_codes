def paciente(n, p, c):
    return {'nome': n, 'prioridade': p, 'carteira': c}

def adiciona_paciente(p, l):
    l.append(p)
    return l
   
def mostra_lista(l):
    for m in l:
       print(40 * '=')
       for k, v in m.items():
          print("{}: {}".format(k.capitalize(),v))
    print(40 * '=')

        

