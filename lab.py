# Test Cases
# M1 = [[1,0,1],
#      [0,0,1],
#      [1,1,1]]

P145 = [[1,1,1],
     [0,0,1],
     [0,0,1]]

MR1 = [[1,0,1],
     [0,0,1],
     [1,1,1]]

MR2 = [[0,1,1,0],
     [1,1,0,0],
     [1,0,1,1],
     [0,0,1,1]]

MR3 = [[1,1,1],
     [0,1,0],
     [0,0,0]]

MR4 = [[0,0,1,1],
     [0,0,1,0],
     [0,0,0,1],
     [1,0,0,0]]

MR5 = [[1,0,0,1],
     [0,1,1,1],
     [0,0,1,0],
     [0,0,0,1]]

MR6 = [[0,1,1,1],
     [0,0,1,0],
     [0,0,0,1],
     [0,0,0,0]]

p146_11 = [[0,1,0,1],
     [1,0,1,1],
     [0,1,0,0],
     [1,1,0,0]]

p146_12 = [[1,1,0,0],
     [1,1,0,0],
     [0,0,1,0],
     [0,0,0,1]]

p151_1 = [[1,0,0],
     [0,1,1],
     [0,1,1]]

p151_2 = [[1,0,1],
     [0,1,0],
     [0,0,1]]

p152_18 = [[1,0,0,0],
     [0,1,1,1],
     [0,1,1,1],
     [0,1,1,1]]

X = [[1,0,1],
     [0,1,1],
     [1,1,1]]

# Symmetric Test
def SymmetricTest(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not matrix[i][j]==matrix[j][i]:
                print("Not Symmetric")
                return
    print("Symmetric")

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
def ReflexsiveTest(matrix):
    for i in range(len(matrix)):
        if not matrix[i][i]==1:
            print("Not Reflexsive")
            return
    print("Reflexsive")

# Irreflexsive Test
def IrreflexsiveTest(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 1:
            print("Not Irreflexsive")
            return
    print("Irreflexsive")

# Transitive
def TransitiveTest(matrix):
    for i in range(len(matrix)):
        for j in range(1, len(matrix)):
            if matrix[i][j]:
                n = 0
                while n < len(matrix):
                    if matrix[j][n]:
                        if not matrix[i][n]:
                            print("Not transitive")
                            return
                    n += 1
    print("Transitive")
    return

# Equivalence Test
def EquivalenceTest(matrix):
    if TransitiveTest(matrix) and ReflexsiveTest(matrix) and SymmetricTest(matrix):
        print("R is an equivalence relation")
    else:
        print("R is not an equivalence relation")
    return

# Complement
def Complement(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            elif matrix[i][j] == 0:
                matrix[i][j] = 1
    for i in range(len(matrix)):
        print("[", end="")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=", " )
        print("]", end="")
        print()

# Inverse
def Inverse(matrix):
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


