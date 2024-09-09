import numpy as np

def exercicio_1():
    #A
    A = np.array([])
    for i in range(0,6):
        A = np.append(A,int(input(f"Digite o {i+1}º valor: ")))
    print(A)
    #B
    print(A[0]+A[1]+A[4])
    #C
    A[4] = 100
    print(A[4])
    #D
    for i in range(0,len(A)):
       print(A[i])
    
def exercicio_2():
    B = np.array([])
    for i in range(0,6):
        B = np.append(B,int(input(f"Digite o {i+1}º Valor: ")))
    print(B)
    
def exercicio_3():
    C = np.array([2,3,4,5,6,7,8,9,10,11])
    D = np.array([])
    for i in range(0,len(C)):
        D = np.append(D,pow(C[i],2))
    print(D)
    
def exercicio_4():
    E = np.array([1,-6,2,7,8,4,2,18])
    x = int(input("Digite x: "))
    y = int(input("Digite y: "))
    print(E[x]+E[y])

def exercicio_5():
    F = np.array([1,2,3,4,5,6,7,8,9,10])
    Fp = np.array([])
    soma = 0
    for i in range(0,9):
        if F[i]%2 == 0:
            soma += 1
            Fp = np.append(Fp,F[i])
    print(Fp)
    print(soma)

def exercicio_6():
    G = np.array([])
    for i in range(0,10):
        G = np.append(G,int(input(f"Digite o {i}º número: ")))
    print(f"Maior valor: {max(G)} \nMenor Valor: {min(G)}")

def exercicio_7():
    H = np.array([1,74,3,97,4,2,74,1,65,200])
    for i in range(0,10):
        if H[i] == max(H):
            print(f"{H}\n{max(H)}\n{i}")

def exercicio_8():
    I = np.array([1,2,3,4,5,6])
    print(I[::-1])

def exercicio_9():
    J = np.array([])
    i = 0
    while i < 6:
        x = int(input(f"Digite o {i+1}º número par: "))
        if x % 2 == 0:
            J = np.append(J,x)
            i += 1
    print(J[::-1])

def exercicio_10():
    K = np.array([])
    for i in range(0,15):
        K = np.append(K, float(input(f"Digite a nota do {i+1} aluno: ")))
    print(sum(K)/len(K))
    
def exercicio_11():
    L = np.array([])
    for i in range(0,10):
        L = np.append(L, float(input(f"Insira o {i+1}º numero possitivo ou negativo: ")))
    print(sum(x for x in L if x > 0))
    print(len([num for num in L if num < 0]))
    
def exercicio_12():
    M = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    print(M)
#    for i in range():
        
#        0 -1    1 20
#        1 -2    2 19
#        2 -3    3 18
#        3 -4    4 17
#        4 -5    5 16
#        5 -6    6 15
#        6 -7    7 14
#        7 -8    8 13
#        8 -9    9 12
#        9 -10   10 11
        
exercicio_12()