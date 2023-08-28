def suma(a, b):
    return a+ b

def resta(a, b):
    return a- b

def multiplicacion(a, b):
    return a* b

def division(a, b):
    if b == 0:
        raise ValueError('No se puede dividir entre cero.')
    return a / b

try:
    a = float(input('Ingrese el primer numero: '))
    b = float(input('Ingrese el segundo numero: '))
    operacion = input('Introduce la operacion a realizar (+, - *, /): ')

    if operacion == '+':
        resultado = suma(a, b)
    elif operacion =='-':
        resultado = resta(a, b)
    elif operacion == '*':
        resultado = multiplicacion(a, b)
    elif operacion == '/':
        resultado = division(a, b)
    else:
        raise ValueError('Operación no válida.')
    print('El resultado es:', resultado)
except ValueError as error:
    print('¡Error!:', error)

