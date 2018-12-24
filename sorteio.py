import random
def sorteio(y):
    lista = []
    for i in range(1, y+1):
        lista.append(i)
    #print(lista)
    z = random.choice(lista)
    print("o numero sorteado foi: {}".format(z))


while True:
    x = 0
    n1 = 0
    dado = int(input('Qual dado vc quer jogar?\n\tD002 - 1\n\tD004 - 2\n\tD006 - 3\n\tD008 - 4\n\tD010 - 5\n\tD012 - 6\n\tD020 - 7\n\tD030 - 8\n\tD100 - 9\n\t>>>>>> '))
    qnt = int(input('Quantos dados? '))
    while x < qnt:
        if (dado == 1):
            sorteio(2)
        elif (dado == 2):
            sorteio(4)
        elif (dado == 3):
            sorteio(6)
        elif (dado == 4):
            sorteio(8)
        elif (dado == 5):
            sorteio(10)
        elif (dado == 6):
            sorteio(12)
        elif (dado == 7):
            sorteio(20)
        elif (dado == 8):
            sorteio(30)
        elif (dado == 9):
            sorteio(100)
        else:
            print("ERROR: Valor invalido, por favor digite um valor entre 1 e 9. EX: 4")
        n1 += z
        x += 1
    print("A soma do(s) {} foi = {}".format(qnt, n1))
