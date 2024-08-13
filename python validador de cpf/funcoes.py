def verificarCpf(cpf):
    if cpf != [""]:
        if len(cpf) == 11:
            return 1
        else:
            return 0
    else:
        return 0
    
#def validarCpf(cpf):
