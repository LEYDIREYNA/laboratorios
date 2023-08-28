def Celcius_a_Fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def Fahrenheit_a_Celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius
try:
    temperatura = float(input('Ingrese la temperatura: '))
    unidad = input('Ingrese la unidad (C o F): ')

    if unidad.upper() == 'C':
        fahrenheit = Celcius_a_Fahrenheit(temperatura)
        print('La temperatura en Fahrenheit es: ', fahrenheit)
    elif unidad.upper() == 'F':
        celcius = Fahrenheit_a_Celcius(temperatura)
        print('La temperatura en Celcius es: ', celcius)
    else:
        print('Unidad no válida. Introduce "C" para Celcius o "F" para Fahrenheit.')
except ValueError:
    print('Error: Introduce un valor correcto.')
    
