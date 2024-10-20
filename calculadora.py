def calcular(valor1,valor2,operacao):
    if ((not valor1.lstrip('-').replace('.','').isnumeric()) 
        or (not valor2.lstrip('-').replace('.','').isnumeric()) 
        or (operacao not in ['+','-','*','/','^'])):
        return None #float('nan')

    valor1 = float(valor1)
    valor2 = float(valor2)
    
    match operacao:
        case '+':
            resultado = valor1 + valor2
        case '-':
            resultado = valor1 - valor2
        case '*':
            resultado =  valor1 * valor2
        case '/':
            if valor2 == float(0):
                return None
            resultado = valor1 / valor2
        case '^':
            resultado = valor1 ** valor2
    return resultado