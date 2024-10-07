def asf():
    a = int(input("a = "))

    x = [[0]*a]
    for i in range(1,a,1):
        x.append([0]*a)

    for i in range(0,a,1):
        for j in range(0,a,1):
            if i == j:
                x[i][j] = 1
    print(x)
def rgsthfj():
    a = [[2,3,1],
        [-1,0,2]]

    b = [[1,-2],
        [0,5],
        [4,1]]

    c = [[0,0],[0,0]]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

    print(c)

x = [[0  ,2  ,11 ,6  ,15 ,11 ,1 ],
     [2  ,0  ,7  ,12 ,4  ,2  ,15],
     [11 ,7  ,0  ,11 ,8  ,3  ,13],
     [6  ,12 ,11 ,0  ,10 ,2  ,1 ],
     [15 ,4  ,8  ,10 ,0  ,5  ,13],
     [11 ,2  ,3  ,2  ,5  ,0  ,14],
     [1  ,15 ,13 ,1  ,13 ,14 ,0]]
def i1():
    a = int(input("a = "))
    b = int(input("b = "))
    print(x[a-1][b-1])

def i2():
    f = 1
    k = 0
    rota = []

    while f > 0:
        f = int(input("f = "))
        rota.append(f)

    for i in range(len(rota)):
        c = rota[i]
        d = rota[i + 1] if i < len(rota) - 1 else c
        k += x[c-1][d-1]
    print(k)
i2()