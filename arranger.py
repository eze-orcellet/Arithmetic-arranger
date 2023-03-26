def arithmetic_arranger(problems, show_result = False):

    if len(problems) > 5:
            return("Error: Too many problems.")

    linea1 = []
    operadores = ["+", "-"]
    linea2 = []
    linea3 = []
    linea4 = []

    for operation in problems:

        each = operation.split(" ")
        primero = each[0]
        operador = each[1]
        segundo = each[2]

        if operador not in operadores:
            return("Error: Operator must be '+' or '-'.")

        if primero.isnumeric() == False or segundo.isnumeric() == False:
            return("Error: Numbers must only contain digits.")
        
        if len(primero) > 4 or len(segundo) > 4:
            return("Error: Numbers cannot be more than four digits.")

        espacios = max(len(x) for x in each)
        rayas = "-"
        space = " "

        resultado = str(eval(operation))

        linea1.append(primero.rjust(espacios + 2) + space * 4)
        linea2.append(operador + space + segundo.rjust(espacios) + space * 4)
        linea3.append(rayas * (espacios + 2) + space * 4)
        linea4.append(resultado.rjust(espacios + 2) + space * 4)

    linea1 = "".join(map(str, linea1))
    linea2 = "".join(map(str, linea2))
    linea3 = "".join(map(str, linea3))
    linea4 = "".join(map(str, linea4))

    if show_result == True:
            arranged_problems = linea1.rstrip() + "\n" + linea2.rstrip() + "\n"+ linea3.rstrip()+ "\n"+ linea4.rstrip()
        
    if show_result == False:
            arranged_problems = linea1.rstrip() + "\n"+ linea2.rstrip() + "\n"+ linea3.rstrip()
    
    
    return print(arranged_problems)

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

arithmetic_arranger(["32 + 8", "1 - 3801", "444 + 666", "523 - 49"], True)
