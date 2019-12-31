from copy import deepcopy
def form_Matrix(l,row ,col):#l: list of inputs row wise
    M = []
    c = 0
    for i in range(row):
        m = []
        for j in range(c,col+c):
            m += [l[j]]
            c += 1
        M += [m]
    return M
def filtermatrix(M):
    N = []
    row = len(M)
    col = len(M[0])
    for i in range(row):
        n = []
        for j in range(col):
            n += [float('%f' % M[i][j])]
        N += [n]
    return N

def sm(M,name):
    print(f'{name} -> ')
    print()
    size = 10
    row = len(M)
    col = len(M[0])
    for i in range(row):
        s = ' '
        for j in range(col):
            z = M[i][j]
            if type(M[i][j]) == complex:
                zreal = z.real
                zimag = z.imag
                if zreal == 0:
                    if zimag > 0:
                        s += '%f' % zimag + 'j'+ ' '*(size - 1 - len(str(int(zimag))))
                    else:
                        s = s[:-1]
                        s += '%f' % zimag + 'j'+ ' '*(size - 1 - len(str(int(abs(zimag)))))
                elif zimag == 0:
                    if zreal > 0:
                        s += '%f' % zreal +' '*(size - len(str(int(zreal))))  
                    else:
                        s = s[:-1]
                        s += '%f' % zreal +' '*(size - len(str(int(abs(zreal)))))
                else:
                    if zreal > 0:
                        if zimag > 0:
                            q = '%.2f' % zreal +'+'+ '%.2f' % zimag + 'j'
                            s += q+' '*(size+2 - len(q))
                        else:
                            q = '%.2f' % zreal + '%.2f' % zimag + 'j'
                            s += q+' '*(size+2 - len(q))
                    else:
                        s = s[:-1]
                        if zimag > 0:
                            q = '%.2f' % zreal +'+'+ '%.2f' % zimag + 'j'
                            s += q+' '*(size +3- len(q))
                        else:
                            q = '%.2f' % zreal + '%.2f' % zimag + 'j'
                            s += q+' '*(size +3- len(q))
            else:
                if z >= 0:
                    s += '%f' % abs(z) + ' '*(size - len(str(int(z))))
                else:
                    s = s[:-1]
                    s += '%f' % z + ' '*(size  - len(str(int(abs(z)))))
        print(s)
    print()
    return

def minor(M,row,col):# M is a sq matrix
    l = []
    for i in range(len(M)):
        if i != row:
            for j in range(len(M)):
                if j != col:
                    l += [M[i][j]]
    return form_Matrix(l,int(len(l)**.5),int(len(l)**.5))# returns a n-1 x n-1 matrix

def  determinant(M):
    D = 0
    if len(M) == 1:
        return M[0][0]
    elif len(M) == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    else:
        for i in range(len(M)):
            sign = (-1)**i
            D += M[i][0]*sign*determinant(minor(M,i,0))# using Laplace's expansion
    return D

def transpose(M):
    row = len(M)
    col = len(M[0])
    N = []
    for i in range(col):
        n = []
        for j in range(row):
            n += [M[j][i]]
        N += [n]    
    return N

def inverse(M):
    N = []
    det = determinant(M)
    if det != 0:
        for i in range(len(M)):
            n = []
            for j in range(len(M)):
                sign = (-1)**(i+j)
                n += [sign*determinant(minor(M,i,j))/det]
            N += [n]
        return transpose(N)
    else:
        print(f'{M} is not invertible')
        return

def product(A,B):
    row1 = len(A)
    row2 = len(B)
    col1 = len(A[0])
    col2 = len(B[0])
    l = []
    if col1 == row2:
        for i in range(row1):
            for j in range(col2):
                s = 0
                for k in range(col1):
                    s += A[i][k]*B[k][j]
                l += [s]
        return form_Matrix(l,row1,col2)
    else:
        print('product undefined')
    return

def trace(M):
    c = 0
    row = len(M)
    col = len(M[0])
    for i in range(row):
        for j in range(col):
            c += M[i][j]
    return c

def conjugatematrix(M):
    N = []
    row = len(M)
    col = len(M[0])
    for i in range(row):
        n = []
        for j in range(col):
            n += [M[i][j].conjugate()]
        N += [n]
    return N

def dagger(M):
    return transpose(conjugatematrix(M))

def aresame(A,B):
    row1 = len(A)
    row2 = len(B)
    col1 = len(A[0])
    col2 = len(B[0])
    if row1 == row1 and col1 == col2:
        c = 0
        for i in range(row1):
            for j in range(col1):
                if A[i][j] == B[i][j]:
                    c += 1
        if c == row1*col1:
            return True
        else:
            return False
    else:
        return False

def Id(sign,n):
    M = []
    for i in range(n):
        m = []
        for j in range(n):
            if i == j:
                m += [sign]
            else:
                m += [0]
        M += [m]
    return M

def Zero(row,col):
    l = [0 for i in range(row*col)]
    return form_Matrix(l,row,col)

def add(A,B):
    C = []
    row1 = len(A)
    row2 = len(B)
    col1 = len(A[0])
    col2 = len(B[0])
    if row1 == row1 and col1 == col2:
        for i in range(row1):
            c = []
            for j in range(col1):
                c += [A[i][j] + B[i][j]]
            C += [c]
        return C
    else:
        print(f'dimensions of {A} and {B} do not match')
        return

def isHermitian(M):
    if aresame(M,dagger(M)):
        return 1
    elif aresame(M,product(dagger(M),Id(-1,len(M)))):
        return -1
    else:
        return 0

def isUnitary(M):
    return aresame(inverse(M),dagger(M))

def isSymmetric(M):
    if aresame(M,transpose(M)):
        return 1
    elif aresame(M,product(Id(-1,len(M)),transpose(M,len(M),len(M[0])))):
        return -1
    else:
        return 0

def isOrthogonal(M):
    return aresame(inverse(M),transpose(M,len(M),len(M[0])))

def commutator(A,B):
    return add(product(A,B),product(Id(-1,len(A)),product(A,B)))

def norm(V):
    if len(V[0]) > len(V):
        return (determinant(product(V,transpose(V))))**.5
    else:
        return (determinant(product(transpose(V),V)))**.5

def normalize(V):
    return product(Id(1/norm(V),len(V)),V)

def GS(M):
    N = transpose(M)
    n = len(N)
    m = len(N[0])
    z = {}
    for i in range(n):
        x = transpose(form_Matrix(N[i],1,m))
        print(f'<v{i}> = ')
        sm(x)
        sub = Zero(m,1)
        for j in range(i):
            sub = add(sub,product(Id(determinant(product(transpose(z[j]),x)),m),z[j]))
        z[i] = normalize(add(x,product(Id(-1,m),sub)))
    for i in range(n):
        print(f'<e{i+1}> = ')
        sm(z[i])
    return

def rowswitch(M,rowi,rowj):
    if rowi > rowj:
        rowj, rowi = rowi, rowj
    temp = M.pop(rowi)
    M.insert(rowi,M.pop(rowj-1))
    M.insert(rowj,temp)
    return M

def colswitch(M,col1,col2):
    N = transpose(M)
    rowswitch(N,col1,col2)
    return transpose(N)

def rowmultiply(M,row,scalar):
    for i in range(len(M[0])):
        temp = scalar * M[row].pop(i)
        M[row].insert(i,temp)
    return M

def rowadd(M,rowi,rowj,scalar):
    N = deepcopy(M)
    rowmultiply(N,rowj,scalar)
    for i in range(len(M[0])):
        temp = M[rowi].pop(i) + N[rowj][i]
        M[rowi].insert(i,temp)
    return M

def zerocounter(l):
    c = 0
    for i in l:
        if i == 0:
            c += 1
    return c

def REF(M):
    row = len(M)
    col = len(M[0])
    rowk = 0
    colk = 0
    while colk < col:
        maxi = rowk
        while colk < col-1:
            for i in range(rowk,row):
                if abs(M[i][colk]) > abs(M[maxi][colk]):
                    maxi = i
            if maxi != rowk:
                rowswitch(M,rowk,maxi)
                break
            elif M[maxi][colk] == 0:
                colk += 1
            else:
                break
        if M[rowk][colk] == 0:
            break
        for i in range(rowk+1,row):
            const = -1*M[i][colk]/M[rowk][colk]
            rowadd(M,i,rowk,const)
        rowmultiply(M,rowk,1/M[rowk][colk])
        rowk += 1
        colk += 1
    return M

def rank(M):
    N = filtermatrix(REF(M))
    c = 0
    row = len(N)
    col = len(N[0])
    for i in range(row):
        if zerocounter(N[i]) != col:
            c += 1
    return c

def GEsolve(M):
    REF(M)
    n = len(M[0]) - 1
    N = transpose(M)
    N.pop(-1)
    rankA = rank(N)
    rankAb = rank(M)
    if rankA == rankAb and rankA == n:
        d = {n-1:M[-1][-1]}
        for i in reversed(range(0,n-1)):
            c = 0
            for j in range(i+1,n):
                c += M[i][j]*d[j]
            d[i] = M[i][-1] - c
        for i in range(n):
            print(f'x_{i+1} = {d[i]}')
    elif rankA == rankAb and rankA < n:
        print('The system has infinite solutions')
    else:
        print('The system has no solutions')
    return

def Cramersolve(M):
    N = transpose(M)
    b = M[-1][:]
    N.pop(-1)
    d = {}
    detM = determinant(N)
    if detM != 0:
        for i in range(len(N)):
            P = transpose(M)
            rowswitch(P,i,len(P)-1)
            P.pop(-1)
            d[i] = determinant(P)/determinant(N)
            P.clear()
        for key,val in d.items():
            print(f'x_{key+1} = {val}')
    elif detM == 0 and zerocounter(b) == len(b):
        print('The system has infinite solutions')
    else:
         print('The system has no solutions')
    return
