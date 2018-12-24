import os

l = []
l2 = []
l3 = []
l4 = []

def usuario(a, b, c, d ,e):
    return{'nome': a, 'email': b, 'login': c, 'senha': d, 'tipo': e}

def idiomas(f, f1):
    return{'idiomas': f, 'aluno': f1}

def hora(g):
    return{'horario': g}

def local(h):
    return{'local': h}

def adiciona_usuario(p):
    l.append(p)
    return l

def adiciona_idioma(p1):
    l2.append(p1)
    return l2

def adiciona_horario(p2):
    l3.append(p2)
    return l3

def adiciona_local(p3):
    l4.append(p3)
    return l4


def mostra_usuario(ti):
    x = (l[ti])
    print(50 * '=')
    print('\nNome: {}'.format(x['nome']))
    print('E-mail: {}'.format(x['email']))
    print('Login: {}'.format(x['login']))
    print('Tipo: {}'.format(x['tipo']))
    print(50 * '=')
    print("\n")
    if x['tipo'] == 'aluno':
        x00 = 0
        while True and x00 != 1:
            opc = int(input('''Digite uma opção:
    1)Para cadastrar e consultar idiomas que deseja estudar 
    2)Para cadastrar e consultar o horario que deseja estudar
    3)Para cadastrar e consultar o local que pretende realizar o curço
    4)Para mostrar sua situaçao
    5)Para sair
    Escolha a opção inicial: '''))
            os.system("cls")
            if opc == 1:
                x01 = 0
                while True and x01 != 1:
                    op1 = int(input('1)Portugues\n2)Ingles\n3)Fances\n4)Espanhol\n5)Voltar\n>>>>> '))             
                    if op1 == 1:
                        idi = 'Portugues'
                        alu = x['nome']
                        adiciona_idioma(idiomas(idi, alu))
                        alu = ''
                        os.system("cls")
                    elif op1 == 2:
                        idi = 'Ingles'
                        alu = x['nome']
                        adiciona_idioma(idiomas(idi, alu))
                        alu = ''
                        os.system("cls")
                    elif op1 == 3:
                        idi = 'Frances'
                        alu = x['nome']
                        adiciona_idioma(idiomas(idi, alu))
                        alu = ''
                        os.system("cls")
                    elif op1 == 4:
                        idi = 'Espanhol'
                        alu = x['nome']
                        adiciona_idioma(idiomas(idi, alu))
                        alu = ''
                        os.system("cls")
                    elif op1 == 5:
                        x01 = 1
                    else:
                        print("ERRO: Por favor digite um valor valido")
            elif opc == 2:
                x02 = 0
                while True and x02 != 1:
                    op2 = int(input('1)Manha\n2)Tarde\n3)Noite\n4)Voltar\n>>>>> '))
                    if op2 == 1:
                        hor = 'Manha'
                        adiciona_horario(hora(hor))
                        os.system("cls")
                    elif op2 == 2:
                        hor = 'Tarde'
                        adiciona_horario(hora(hor))
                        os.system("cls")
                    elif op2 == 3:
                        hor = 'Noite'
                        adiciona_horario(hora(hor))
                        os.system("cls")
                    elif op2 == 4:
                        x02 = 1
                    else:
                        print("ERRO: Por favor digite um valor valido")
            elif opc == 3:
                x03 = 0
                while True and x03 != 1:
                    op3 = int(input('1)Mossoro\n2)Natal\n3)Voltar\n>>>>> '))
                    if op3 == 1:
                        loc = 'Mossoro'
                        adiciona_local(local(loc))
                        os.system("cls")
                    elif op3 == 2:
                        loc = 'Natal'
                        adiciona_local(local(loc))
                        os.system("cls")
                    elif op3 == 3:
                        x03 = 1
                    else:
                        print("ERRO: Por favor digite um valor valido")
            elif opc == 4:
                x00 = 1
            else:
                print("ERRO: Por favor digite um valor valido")
    else:
        x10 = 0
        while True and x10 != 1:
            opd = int(input('''Digite uma opção:
    1)Para cadastrar notas
    2)Para colocar faltas
    3)Materias que esta ministrando
    4)Para sair
    Escolha a opção inicial: '''))
            os.system("cls")
            if opd == 1:
                print("Indisponovel no momento")
                
            elif opd == 2:
                print("Indisponivel no momento")
            elif opd == 3:
                print("Indisponivel no momento")
            elif opd == 4:
                x10 = 1
            else:
                print("ERRO: Por favor digite um valor valido")
        os.system("cls")    
    print("\n")

 
print("\n")
print(50 * '~')
while True or op != 2:
    op = int(input('''Digite uma opção:
    1)Pressione 1 para adicionar usuarios 
    2)Pressione 2 para sair
    3)Pressione 3 mostrar usuarios cadastrados
    4)Pressione 4 para fazer login
    Escolha a opção inicial: '''))
    print("\n")
    print(50 * '=')

    if op == 1:
        print("\n")
        nome = input('Digite o nome do usuario: ')
        email = input('Digite o E-mail do usuario: ')
        login = input('Digite o login do usuario: ')
        senha = input('Digite a senha do usuario: ')
        tipo = input('Digite o tipo do usuario (professor/aluno): ')
        adiciona_usuario(usuario(nome, email, login, senha, tipo))
        os.system("cls")
        print(50 * '=')
    elif op == 2:
        print('\nFIM\n')
        print(50 * '~')
        os.system("cls")
        break
    elif op == 3:
        print(50 * '=')
        mostra_usuario()
    elif op == 4:
        log = str(input('Login: '))
        sen = str(input('senha: '))
        nul = len(l)
        aux = 0
        axu = 0
        while aux < nul and axu < 1:
            if log == l[aux]['login']:
                if sen == l[aux]['senha']:
                    os.system("cls")
                    mostra_usuario(aux)
                    

                
                else:
                    print("ERROR: Senha invalida")
                axu = 1
            else:
                aux += 1
                if aux == nul:
                    print("eRROR: Usuario inesistente")
    else:
        print("\nERRO: Resposta invalida. Por favor digite um valor valido!\n")
    
