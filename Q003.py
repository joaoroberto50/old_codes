mtz1 = [[1,6,8,11],[3,1,0,-3],[9,-6,-2,0],[0,-1,3,7]]
mtz2 = [[-3,0,0,0],[1,6,0,-1],[-3,9,5,-2],[0,0,1,-4]]

print("{} = Matriz A\n{}\n{}\n{}".format(mtz1[0],mtz1[1],mtz1[2],mtz1[3]))
print("\n{} = Matriz B\n{}\n{}\n{}\n".format(mtz2[0],mtz2[1],mtz2[2],mtz2[3]))

mtz3 = []
for x in range(len(mtz1)):   
    mtz3.append([])
    for y in range(len(mtz1[0])):
        mtz3[x].append(mtz1[x][y] + mtz2[x][y])
        print(mtz3)
    print("\n")
print("{} = Matriz A + B\n{}\n{}\n{}".format(mtz3[0],mtz3[1],mtz3[2],mtz3[3]))
