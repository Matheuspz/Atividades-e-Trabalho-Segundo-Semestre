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

exercicio_4()