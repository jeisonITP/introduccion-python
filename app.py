# Este es un comentario de una sola linea
"""
    Este es un comentario
    de multiple linea
"""

'''
    Este es otro comentario
    de multiple linea
    con comillas sencillas
'''

#Variables
nombre = 'jeyson' # String
cantidadMaterias = 3 # Integer
numeroDecimal = 17.2 # Float

diasSemana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'] # Listas = Array
listaDinamica = [0, 'Hola', 12.5, [0, 1]]

print(diasSemana[2]) # Miercoles
print(listaDinamica[3][1]) # [0, 1] # 1

esMayorEdad = False

#Diccionarios - JSON - Objects
persona = {
    'nombre': 'Jeyson',
    'apellido': 'Calvache',
    'edad': 27,
    'materias': ['Base de datos II', 'Lenguaje de cuarta generacion'],
}

print(persona['nombre']) # Jeyson
print(persona['materias'][1]) # Lenguaje de cuarta generacion
print(persona)

# Lista de diccionarios
personas = [
    {
        'nombre': 'Jeyson',
        'apellido': 'Calvache',
        'edad': 27,
        'materias': ['Base de datos II', 'Lenguaje de cuarta generacion'],
    },
    {
        'nombre': 'Juan',
        'apellido': 'Perez',
        'edad': 26,
        'materias': ['Base de datos I', 'Lenguaje Orientado a Objetos'],
    },
    {
        'nombre': 'Pepito',
        'apellido': 'Perez',
        'edad': 25,
        'materias': ['Lenguaje Orientado a Eventos'],
    }
]
print(personas[2]['materias'][0]) #Lenguaje Orientado a Eventos

# Condiciones
esMayorEdad = True

if esMayorEdad:
    print('Es mayor de edad')
    print('Esto es del if')
else:
    print('No es mayor de edad')
    print('Esto es parte del else')

print('mensaje de prueba')

for per in personas:
    print(per['nombre'])
    
nombrePersona = 'roberto'

print(nombrePersona[2])
    

