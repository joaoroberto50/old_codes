x = 0
lista = []
y = 0
b = 0
k = 0

while x < 25:
    num = int(input('\t>>> '))
    while k < 1:
        y = num
        b = num
        k += 1
    lista.append(num)
    if num >= y:
        y = num
    if num <= b:
        b = num 
    x += 1
    
q = lista.index(y)
t = lista.index(b)

cont = 0
for i in lista:
    cont += i
med = cont/25

con = 0
for a in lista:
    con += ((a - med)**2)
di = con/25
dp = di**0.5

print(33 * '~')
print("A media da lista = {}".format(med))
print(33 * '=')
print("Maior = {}; e sua posicao eh: {}".format(y, q))
print(33 *'-')
print("Menor = {}; e sua posicao eh: {}".format(b, t))
print(33 * '=')
print("Desvio padrao = {:.2}".format(dp))
print(33 * '~')
