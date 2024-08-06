#EXERCÍCIO 1
#----------------//------------------
def maior_valor(x,y,z):
    return max(x,y,z)
def exercicio1():
    a = int(input("Valor 1: "))
    b = int(input("Valor 2: "))
    c = int(input("Valor 3: "))
    print(maior_valor(a,b,c))
#----------------//------------------

#EXERCÍCIO 2
#----------------//------------------
def perimetoTriangulo(x,y,z):
    return (x+y+z)
def exercicio2():
    a = int(input("Lado 1: "))
    b = int(input("Lado 2: "))
    c = int(input("Lado 3: "))
    print(perimetoTriangulo(a,b,c))
#----------------//------------------

#EXERCÍCIO 3
#----------------//------------------
def calcular_conceito(x):
    if x >= 9 and x <= 10:
        return "A"
    elif x >= 8 and x < 9:
        return "B"
    elif x >= 7 and x < 8:
        return "C"
    elif x >= 6 and x < 7:
        return "D"
    elif x < 6:
        return "F"
    else:
        return "Nota Inválida"
def exercicio3():
    x = float(input("Digite uma nota: "))
    print(calcular_conceito(x))
#----------------//------------------

#EXERCÍCIO 4
#----------------//------------------
def verificarAprovacao(total_aulas,num_faltas,nota):
    presenca = total_aulas - num_faltas
    porcentagem_presenca = presenca/total_aulas
    
    if num_faltas < 0 or total_aulas < 0:
        return "Quantidade de Faltas ou Aulas Invalidas"
    elif num_faltas > total_aulas:
        return "Quantidade de Faltas Invalidas"
    if nota < 0 or nota > 10:
        return "Nota Invalida"
    elif porcentagem_presenca < 0.25 or nota < 6:
        return 0
    else:
        return 1
def exercicio4():
    a = int(input("Digite qnt de aulas: "))
    b = int(input("Digite qnt de faltas: "))
    c = float(input("Digite a nota: "))
    print(verificarAprovacao(a,b,c))
#----------------//------------------

#EXERCÍCIO 5
#----------------//------------------
def classeEleitoral(idade):
    if idade < 0:
        return "Valor Inválido"
    elif idade < 16:
        return "Não eleitor"
    elif idade >= 16 and idade < 18 or idade > 65:
        return "Eleitor facultativo"
    elif idade >= 18:
        return "Eleitor obrigatorio"
    else:
        return "Valor Inválido"
def exercicio5():
    x = int(input("Digite sua idade: "))
    print(classeEleitoral(x))
#----------------//------------------
