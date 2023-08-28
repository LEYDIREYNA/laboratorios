import random
import string
def generar_contraseña(longitud, mayus=True, minus =True, nums=True, especial=True ):
    try:
        caracteres = ''
        if mayus:
            caracteres += string.ascii_uppercase
        if minus:
            caracteres += string.ascii_lowercase
        if nums:
            caracteres += string.digits
        if especial:
            caracteres += string.punctuation

        if not caracteres:
            raise ValueError('Debe seleccionar por lo menos un tipo de caracter.')
        
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        return contraseña
    except ValueError as error:
        print('¡Error!:', error)
        

contraseña = generar_contraseña(10, mayus=True, minus=True, nums=True, especial=True)
print('contraseña generada: ', contraseña)
