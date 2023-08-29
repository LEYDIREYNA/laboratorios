def cifrado_cesar(mensaje, desplazar):
    mensaje_cifrado = ''
    for caracter in mensaje:
        if caracter.isalpha(): 
            codigo_ascii = ord(caracter)
            codigo_cifrado = codigo_ascii + desplazar
            if caracter.isupper():
                if codigo_cifrado > ord('Z'):
                    codigo_cifrado -= 26
                elif codigo_cifrado < ord('A'):
                    codigo_cifrado += 26
            else:
                if codigo_cifrado > ord('z'):
                    codigo_cifrado -= 26
                elif codigo_cifrado < ord('a'):
                    codigo_cifrado += 26
            caracter_cifrado = chr(codigo_cifrado)
        else:
            caracter_cifrado = caracter 
        mensaje_cifrado += caracter_cifrado
    return mensaje_cifrado

mensaje_cifrado = cifrado_cesar('HOLA PHYTON', 2)
print(mensaje_cifrado)
