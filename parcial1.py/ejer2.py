from lista import Lista
from random import randint

lista_personajes = lista[]
lista_aux = ['Black Cat', 'Hulk', 'Rocket Racoonn', 'Loki']
cola = cola[]


class Personajes:

    def __init__(self, nombreHeroe, nombrePersonaje, grupo, anio_aparicion)
        self.nombre = nombreHeroe
        self.nombrePersonaje = nombrePersonaje
        self.grupo = grupo
        self.anio_aparicion = anio_aparicion
    def __str__(self):
        return '{self.nombreHeroe} - {self.nombrePersonaje} - {self.grupo} - {self.anio_aparicion}'   
    


Personajes = [
{'nombreHeroe': 'Antorcha Humana', 'nobrePersonaje': 'Jonathan Storm','grupo': '4 Fantasticos', 'anio_aparicion': '1961'}
{'nombreHeroe': 'Capitana Marvel','nombrePersonaje': 'Carol Dnvers' , 'grupo': '', 'anio_aparicion': '1968'}
{'nombreHeroe': 'Capitan America',' nobrePersonaje': 'Steves Rogers','grupo': 'Avengers', 'anio_aparicion': '1941'}
{'nombreHeroe': 'Ciclope',' nobrePersonaje': 'Scott Summers','grupo': 'X Men', 'anio_aparicion': '1963'}
{'nombreHeroe': 'Drax el Destructor', 'nombrePersonaje': 'Drax', 'grupo': 'Guardianes de la Galaxia', 'anio_aparicion': '1973'}
{'nombreHeroe': 'Dr.Strange','nombrePersonaje': 'Stephen Strange', 'grupo': '','anio_aparicion': '1963' }
{'nombreHeroe': 'Iron Man','nombrePersonaje': 'Tony Stark' , 'grupo': 'Avengers', 'anio_aparicion': '1963'}
{'nombreHeroe': 'Gamora', 'nombrePersonaje':'', 'grupo': 'Guardianes de la Galaxia', 'anio_aparicion': '1975'}
{'nombreHeroe': 'Groot', 'nombrePersonaje': 'grupo': 'Guardianes de la Galaxia', 'anio_aparicion': '1960'}
{'nombreHeroe': 'Hulk',' nobrePersonaje': 'Bruce Baners','grupo': 'Avengers', 'anio_aparicion': '1962'}
{'nombreHeroe': 'La Mole', 'nobrePersonaje': 'Benn Grimm','grupo': '4 Fantasticos', 'anio_aparicion': '1961'}
{'nombreHeroe': 'Mujer Invisible', 'nobrePersonaje': 'Susan Atorm','grupo': '4 Fantasticos', 'anio_aparicion': '1961'}
{'nombreHeroe': 'Sr Fantastico', 'nombrePersonaje': 'Reed Rechards','grupo': '4 Fantasticos', 'anio_aparicion': '1961'}
{'nombreHeroe': 'Star Lord', 'nombrePersonaje': 'Peter Quill' , 'grupo': 'Guardianes de la Galaxia', 'anio_aparicion': '1976' }
{'nombreHeroe': 'Thor','nobrePersonaje': '','grupo': 'Avengers', 'anio_aparicion': '1962'}
{'nombreHeroe': 'Vlack Widow', 'nombrePersonaje':'Natasha Romanov', 'grupo': 'Avengers','anio_aparicion': '1964' }
{'nombreHeroe': 'Profesor X', 'nobrePersonaje':'Charles Xavier','grupo': 'X Men', 'anio_aparicion': '1963'}
{'nombreHeroe': 'Jean Grey',' nobrePersonaje': '','grupo': 'X Men', 'anio_aparicion': '1963'}
{'nombreHeroe': 'Storm',' nobrePersonaje': 'Ororo Monroe','grupo': 'X Men', 'anio_aparicion': '1963'}
{'nombreHeroe': 'Wolverine','nombrePersonaje': 'Logan', 'grupo': 'X Men','anio_aparicion': '1974'}
]


#!A
print('Personaje buscado:')
personajeBuscado = ['Capitana Marvel']
for buscar in personajes:
    datos =  lista_personajes.buscar(buscar, 'personaje')
    if lista.get_element_by_index(i).personaje == 'Capitana Marvel':
    print('El nombre del personaje que interpreta a la Capitana Marvel es: ' lista.get_element_by_index(i))  
    elif
    print('El personaje no se encuentra en la li8sta')


#!B
class Cola:
cola.append("Superhéroe1")
cola.append("Superhéroe2")
cola.append("Superhéroe3")
cola.append("Superhéroe4")
print('Los heroes que pertenecen al grupo Guardianes de la Glaxia son: ' cola[])
     
     
#!C
cuatro_fantasticos = ["Sr. Fantástico", "Mujer Invisible", "Antorcha Humana", "La Mole"]
guardianes_galaxia = ["Star-Lord", "Gamora", "Drax el Destructor", "Rocket Raccoon", "Groot"]
lista_descendente = list(reversed(lista))

def cuatro_fantasticos.reverse()
def guardianes_galaxia.reverse() 

for descendente in lista_descendente:
     datos = lista_descendente.personajes == 'Cuatro Fantasticos', 'Guardianes de la galaxia':
print("Superhéroes de Los Cuatro Fantásticos (en orden descendente):", cuatro_fantasticos)
print("Superhéroes de los Guardianes de la Galaxia (en orden descendente):", guardianes_galaxia)    


#!D
print('Personajes aparecidos despues de 1960':)
if anio_aparicion > 1960 in lista_Personajes:
   if lista.get_element_by_index(i).nombre == ' ':
        print ('Los superheroes aparecidos despues del 1960son: ', lista.get_element_by_index(i)) 

#!E
edit = input('Cambiar nombre Vlack Widow')
        if edit in Lista:
            newValue = input(f'Cambiar de Vlack Widow a Black WIdow{edit}: ')
            findAndReplace(Lista,edit,newValue)
            print('Se ha cambiado exitosamente')

#!F
lista_aux.append(lista_aux)
def agregar_personajes(personajes_auxiliares): 
    personajes = ['Black Cat', 'Hulk', 'Rocket Racoonn', 'Loki'] 
    for personaje_auxiliar in personajes_auxiliares: 
        if personaje_auxiliar not in personajes_principales: 
            personajes.append(personaje_auxiliar) 
            return personajes
personajes_auxiliares = ['Black Cat', 'Hulk', 'Rocket Racoonn', 'Loki'] 

personajes = agregar_personajes(personajes_auxiliares) 
print(personajes)


#!G
for personaje in personajes:
    if personaje.startswith(('C', 'P', 'S')):
    print('Personajes con C, P o S')
