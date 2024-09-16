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
    N = np.array([])
    print(M)
    for i in range(1,21):
        N = np.append(N, M[-i])
    print(N)
        
def exercicio_13():
    numCand = int(input("Digite a quantidade de candidatos: "))
    numVot = int(input("Digite a quantidade de votantes: "))
    O = np.array([], dtype=object)
    for i in range(0,numCand):
        O = np.append(O, i+1)
    P = np.array([], dtype=object)
    for i in range(0,numVot):
        P = np.append(P, int(input("")))
    valido = np.isin(P,O)
    P[~valido] = None
    x,y = np.unique(P[P != None], return_counts=True)
    print(np.asarray((x,y)).T)
    
def exercicio_14():
    #Código com a função SET do python
    #Q = set(range(1,100))
    #R = int(input("Digite nova matricula: "))
    #if R in Q:
    #    print("ERROR!")
    #    print("Matricula já existente")
    #else:
    #    Q.add(R)
    #    print("Matricula adicionada")
    
    #Código com Array
    Q = np.array(range(1,100))
    R = int(input("Digite nova matricula: "))
    if np.isin(R,Q):
        print("ERROR!")
        print("Matricula já existente")
    else:
        Q = np.append(Q,R)
        print("Matricula Adicionada")
        
def exercicio_15():
    S = np.array(range(1,255,3))
    Sp = np.array([])
    Si = np.array([])
    for i in S:
        if i % 2 == 0:
            Sp = np.append(Sp,i)
        else:
            Si = np.append(Si,i)
    print("Pares: ", Sp)
    print("Impares: ", Si)

def exercicio_16():
    #A)
    A1 = np.array(range(1,53,4))    
    A2 = np.array(range(76,254,7))
    A = np.concatenate((A2,A1))
    A = np.sort(A)                  #Criação do Array A
    #Não estava com vontade de pensar em numeros então fiz dessa maneira
    B1 = np.array(range(540,21,-6))
    B2 = np.array(range(63,237,3))
    B = np.concatenate((B1,B2))     
    B = np.sort(B)                  #Criação do Array B
    #Não estava com vontade de pensar em numeros então fiz dessa maneira
    #B/C)
    N = len(A)
    M = len(B)
    C = np.zeros(N + M, dtype=int)
    i = j = k = 0 
    while i < N and j < M:
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1
    while i < N:
        C[k] = A[i]
        i += 1
        k += 1
    while j < M:
        C[k] = B[j]
        j += 1
        k += 1
    print(C)
    #da para resumir isso em 2 linhas: C = np.concatenate((A,B)); C = np.sort(C)
    
def exercicio_17():
    notas = np.array([9.9, 9.7, 9.8, 10, 10])
    x = min(notas)
    y = max(notas)
    media = np.mean(notas[(notas != y) & (notas != x)])
    print(media)
    
exercicio_17()

