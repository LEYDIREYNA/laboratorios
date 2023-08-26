persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True, 
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}
if 'skills' in persona:       #a
    habilidades = persona['skills']
    if len(habilidades) >=3:
        habilidades = habilidades[len(habilidades)//2]
        print('la habilidad del medio es:', habilidades)

if 'skills' in persona and 'Phyton' in persona['skills']:          #b
    print('tiene la habilidad "Phyton".')

if 'skills' in persona:
    if set(habilidades)== {'JavaScript', 'React'}:
        print("él es un desarrollador forntend")
    elif set(habilidades)== {'Node', 'Phyton', 'MogoDB'}:
        print('él es un desarrollador backend')
    elif set(habilidades) == {'React', 'Node', 'MongoDB'}:
        print('él es un desarrollador fullstack')
    else:
        print('título desconocido')
        
