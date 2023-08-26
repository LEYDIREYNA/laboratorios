import string
import random
min = string.ascii_lowercase
mayus = string.ascii_uppercase
num = string.digits
caract_esp = string.punctuation
longitud = 8
total_caracteres = min+mayus+num+caract_esp
pasword = random.sample(total_caracteres, longitud)
contraseña = ''.join(pasword)
print(f'la contraseña creada es: {contraseña}')
