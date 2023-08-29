def es_palindromo(frase):
    frase = frase.lower().replace(' ', '').replace(',', '').replace('.', '').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    frase_invertida = frase[::-1]
    if frase == frase_invertida:
        return True
    else:
        return False
    
frases = input('introduzca una frase: ')
print(es_palindromo(frases))
