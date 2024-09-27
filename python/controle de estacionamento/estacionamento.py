import numpy as np

#Setores
A = np.array([])
B = np.array([])
C = np.array([])


def OcuparVaga():
    placa = input("Insira a placa do veículo: ")
    if np.isin(placa, A, invert=True) or np.isin(placa, B, invert=True) or np.isin(placa, C, invert=True):
        raise Exception("Veículo com placa indicada já resistrado.")
    x = np.random.randint(1,4)