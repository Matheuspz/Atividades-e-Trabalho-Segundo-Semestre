import numpy as np

def execicio_1():
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
    print(A, sep="\n")
    #for i in range(0,len(A)):
    #    print(A[i])
    
def execicio_2():
    B = np.array([])
   
    
execicio_1()