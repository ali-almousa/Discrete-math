import copy
# Test Cases



# Symmetric Test
def SymmetricTest(matrix, Print=1):
    for i in range(len(matrix)):
        #print(i,"i")
        for j in range(len(matrix[i])):
            #print(j,"j")
            if not matrix[i][j]==matrix[j][i]:
                #print(matrix[i][j],matrix[j][i])
                if Print == 1: print("Not Symmetric")
                return 0
    if Print == 1: print("Symmetric")
    return 1

# Antisymmetric Test
def AntisymmetricTest(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 1:
                print("Not Antisymmetric")
                return
    print("Antisymmetric")

# Asymmetric Test
def AsymmetricTest(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and matrix[j][i] == 1:
                print("Not Asymmetric")
                return
    print("Asymmetric")

# Reflexsive Test
def ReflexsiveTest(matrix, Print=1):
    for i in range(len(matrix)):
        if not matrix[i][i]==1:
            if Print == 1: print("Not Reflexsive")
            return 0
    if Print == 1: print("Reflexsive")
    return 1

# Irreflexsive Test
def IrreflexsiveTest(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 1:
            print("Not Irreflexsive")
            return
    print("Irreflexsive")

# Transitive
def TransitiveTest(matrix, Print=1):
    #print(len(matrix), "mat")
    for i in range(len(matrix)):
        #print(i,"i")
        for j in range(1, len(matrix)):
            #print(j,"j")
            if matrix[i][j]:
                #print(matrix[i][j])
                n = 0
               # print(n, "n")
                while n < len(matrix):
                    if matrix[j][n]:
                        if not matrix[i][n]:
                            if Print == 1: print("Not transitive")
                            return 0
                    n += 1

    if Print == 1:print("Transitive")
    return 1

# Equivalence Test
def EquivalenceTest(matrix):
    if TransitiveTest(matrix, Print=0)==1 and ReflexsiveTest(matrix, Print=0)==1 and SymmetricTest(matrix, Print=0)==1:
        print("R is an equivalence relation")
    else:
        print("R is not an equivalence relation")
    return

# Complement
def Complement(matrix):
    temp = copy.deepcopy(matrix)
    print("Complement")
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == 1:
                temp[i][j] = 0
            elif temp[i][j] == 0:
                temp[i][j] = 1
    for i in range(len(temp)):
        print("[", end="")
        for j in range(len(temp[i])):
            print(temp[i][j], end=", " )
        print("]", end="")
        print()

# Inverse
def Inverse(matrix):
    print("Inverse")
    temp = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[j][i])
        temp.append(row)

    for i in range(len(temp)):
        print("[", end="")
        for j in range(len(temp[i])):
            print(temp[i][j], end=", " )
        print("]", end="")
        print()




row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))
testmx = []
for r in range(row):
    demmx = []
    for j in range(col):
        drow = int(input("Enter the index " + "(" + str(r) + ", " + str(j) + ")" + ": "))
        demmx.append(drow)
    print()
    testmx.append(demmx)

for i in range(row):
    for j in range(col):
        print(testmx[i][j], end=" ")
    print()


xopp=eval(input("Enter 1 for all tests or 0 for specific one "))
if xopp==0:
    xop = input("Enter what test you want to try (no capital letters) :")
    if xop == "symmetric":
        SymmetricTest(testmx)
    elif xop == "asymmetric":
        AsymmetricTest(testmx)
    elif xop=="antisymmetric":
        AntisymmetricTest(testmx)
    elif xop=="reflexive":
       ReflexsiveTest(testmx)
    elif xop=="irreflexive":
       IrreflexsiveTest(testmx)
    elif xop=="transitive":
       TransitiveTest(testmx)
    elif xop=="equivalence":
       EquivalenceTest(testmx)
    elif xop=="complement":
        Complement(testmx)
    elif xop=="inverse":
        Inverse(testmx)
    else:
        print("check the spelling")
else:
    SymmetricTest(testmx)
    AsymmetricTest(testmx)
    AntisymmetricTest(testmx)
    ReflexsiveTest(testmx)
    IrreflexsiveTest(testmx)
    TransitiveTest(testmx)
    EquivalenceTest(testmx)
    Complement(testmx)
    Inverse(testmx)
