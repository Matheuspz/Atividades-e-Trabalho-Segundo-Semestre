def verificarCpf(cpf):
    if cpf != [""]:
        if len(cpf) == 11:
            return 1
        else:
            return 0
    else:
        return 0
    
def validarCpf(cpf):
    x = []
    y = [10,9,8,7,6,5,4,3,2]
    for i in range(0,9):
        a = (cpf[i]*y[i])
        x.append(a)
    soma = sum(x)
    modulo = soma%11
    first_dig = 11-modulo
    x = []
    y = [11,10,9,8,7,6,5,4,3,2]
    for i in range(0,10):
        a = (cpf[i]*y[i])
        x.append(a)
    soma = sum(x)
    modulo = soma%11
    second_dig = 11-modulo
    if first_dig == cpf[9] and second_dig == cpf[10]:
        return "CPF Válido"
    else:
        return "CPF INVÁLIDO"