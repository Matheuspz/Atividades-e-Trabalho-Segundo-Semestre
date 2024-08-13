import re
from funcoes import *

x = 0
cpf = input("Digite o cpf: ")
while x == 0:
    if re.search(r"[.-]", cpf):
        if re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf):
            x = 1
        else:
            cpf = input("CPF não válido para análise: ")
    else:
        x = 1
    
    
cpf = re.sub(r"[^0-9]","",cpf)
#x = verificarCpf(cpf)
#print(x)