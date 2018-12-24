def paciente(n, p, c):
    return {'nome': n, 'prioridade': p, 'carteira': c}

def adiciona_paciente(p, l):
    l.append(p)
    return l
   
def mostra_lista(l):
    for m in l:
       print(60 * '=')
       for k, v in m.items():
          print("{}: {}".format(k.capitalize(),v))
    print(60 * '=')



lista_pacientes = []
lista_medicos = [
    { "nome": "Notreve", "especialidade": "Cardiologista", 'pacientes': [nome]},
    { "nome": "Angelica", "especialidade": "Oncologista", 'pacientes': [nome]} ,
    { "nome": "Alexsandra", "especialidade": "Psicóloga", 'pacientes': [nome]} ,
    { "nome": "Lima da FANAT", "especialidade": "Neurologista", 'pacientes': [nome]} 
    ]

while True:
    op = input("""
1) Para adicionar pacientes
2) Para mostrar pacientes
3) Para mostrar médicos
   Digite uma opção: """)
    
    if op == 'q':
        exit()
    
    if op == '1':
        nome = input("Digite o nome do paciente: ")
        prio = input("O paciente é prioridade (sim|nao): ")
        cart = input("Digite o numero da carteira: ")
        medi = input("digite o tipo de atendimento: ")
        adiciona_paciente(paciente(nome, prio, cart), lista_pacientes)
        
    if op == '2':
        mostra_lista(lista_pacientes)
    
    if op == '3':
        mostra_lista(lista_medicos)
    
