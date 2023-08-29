edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#a
edades.sort()
edad_min = edades[0]
edad_max = edades[-1]
print("edad minima:", edad_min)
print('edad maxima:', edad_max)
#b
agregar1 = edades.append(18)
agregar2 = edades.append(27)
edades.sort()
print(edades)
#c
import statistics
edad_media = statistics.median(edades)
print('Edad media:', edad_media)
#d
edad_prom = sum(edades)/len(edades)
print('Edad promedio:', edad_prom)
#e
rango_edades = edad_max - edad_min
print('Rango de edades:', rango_edades)
#f
diferencia_min = abs(edad_min - edad_prom)
diferencia_max = abs(edad_max - edad_prom)
print('Diferencia entre el minimo y promedio:', diferencia_min)
print('Diferencia entre el maximo y promedio:', diferencia_max)