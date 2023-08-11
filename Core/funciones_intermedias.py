#1- Actualizar valores en diccionarios y listas
#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 

def cambiarValor(mi_lista, antiguo_numero, nuevo_numero):
    for lista in mi_lista:
        for i in range(len(lista)):
            if lista[i] == antiguo_numero:
                lista[i]= nuevo_numero
    print(mi_lista)

cambiarValor(x, 10, 15)

#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def cambiarApellido(estudiantes, apellido_actual, apellido_nuevo):
    for estudiante in estudiantes:
        if estudiante['last_name'] == apellido_actual:
            estudiante['last_name']= apellido_nuevo
    print(estudiantes)

cambiarApellido(estudiantes, 'Jordan', 'Bryant')

#En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

def cambiarJugador(directorio, jugador_actual, nuevo_jugador):
    for deportes, jugadores in directorio.items():
        for i in range(len(jugadores)):
            if jugadores[i] == jugador_actual:
                jugadores[i]= nuevo_jugador
    print(directorio)

cambiarJugador(directorio_deportes, 'Messi', 'Andrés')

#Cambia el valor 20 en z a 30.
z = [ {'x': 10, 'y': 20} ]

def cambiarNumero(lista_diccionarios, num_actual, num_nuevo):
    for diccionario in lista_diccionarios:
        for clave, valor in diccionario.items():
                if valor == num_actual:
                    diccionario[clave]= num_nuevo
    print(lista_diccionarios)

cambiarNumero(z, 20, 30)

#2- Iterar a través de una lista de diccionarios
estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(lista_diccionarios):
    for diccionario in lista_diccionarios:
        for clave, valor in diccionario.items():
            print(f"{clave} - {valor}", end=", ")
        print()

iterateDictionary(estudiantes)

#3- Obtener valores de una lista de diccionarios
def iterateDictionary(key_name, some_list):
    for diccionario in some_list:
        if key_name in diccionario:
            valor = diccionario[key_name]
            print(valor)

iterateDictionary("first_name", estudiantes)

#4- Iterar a través de un diccionarios con valores de lista
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dictionary):
    for clave, lista in some_dictionary.items():
        cantidad_valores= len(some_dictionary[clave])
        clave_mayuscula= clave.upper()
        print(f"{cantidad_valores} {clave_mayuscula}")
        for elemento in lista:
            print(elemento)
        print()

printInfo(dojo)







