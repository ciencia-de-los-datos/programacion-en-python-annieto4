"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    import csv

    with open("data.csv", newline='') as f:
        datos = csv.reader(f, delimiter='\t')
        colums = list(datos)

    suma = 0
    for num in colums:
        suma += int(num[1])

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
	t
    """

    import csv
    with open("data.csv", newline='') as f:
        datos = csv.reader(f, delimiter='\t')
        colums = list(datos)

    lista_vocales = []
    vouels = []
    for vouel in colums:
        vouels.append(vouel[0])

    for i in vouels:     
        mi_tupla = (i, vouels.count(i))
        lista_vocales.append(mi_tupla)

    return sorted(set(lista_vocales))


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    t    
    """
    import csv
    with open("data.csv", newline='') as f:
        datos = csv.reader(f, delimiter='\t')
        columns = list(datos)

    vocales = []
    valores = []
    resultado = []
    suma = 0
    for values in columns:
        valores.append((values[0], values[1]))
        vocales.append(values[0])
    
    for vo in set(vocales):
        for v, n in valores:
            if v == vo:
                suma += int(n)
        resultado.append((vo, suma))
        suma = 0          

    return sorted(resultado)

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from operator import itemgetter

    with open('data.csv', 'r') as f:
        data = f.readlines()

    data = [row.split('\t') for row in data]
    data = [row[2] for row in data]
    months = [row[5:7] for row in data]

    mesesCantidad = {}

    for mes in months:
        if mes in mesesCantidad.keys():
            mesesCantidad[mes] = mesesCantidad[mes] + 1
        else:
            mesesCantidad[mes] = 1

    tuplas = [(key, val) for key, val in mesesCantidad.items()]
    resultado = sorted(tuplas, key=itemgetter(0))
    return resultado

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    from operator import itemgetter

    with open('data.csv', 'r') as f:
        data = f.readlines()


    data = [row.split('\t') for row in data]
    data = [row[:2] for row in data]
    
    resultados = {}
   
    for letra, valor in data:
        valor = int(valor)
        if letra in resultados.keys():
            resultados[letra].append(valor)
        else:
            resultados[letra] = [valor]

    tupla = [(key, max(valor), min(valor)) for key, valor in resultados.items()]
    tupla = sorted(tupla, key=itemgetter(0))
        
    return tupla


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    from operator import itemgetter

    with open('data.csv', 'r') as f:
        data = f.readlines()

    data = [row.split('\t') for row in data]
    data = [row[4] for row in data]
    data = [row[:-1] for row in data]
    data = [row.split(',') for row in data]

    resultado = dict()

    for row in data:
        for dupla in row:
            key, valor = dupla.split(':')
            valor = int(valor)
            if key in resultado.keys():
                resultado[key].append(valor)
            else:
                resultado[key] = [valor]

    tupla = [(key, min(valor), max(valor)) for key, valor in resultado.items()]
    tupla = sorted(tupla, key=itemgetter(0))

    return tupla

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    from operator import itemgetter

    with open('data.csv', 'r') as file:
        data = file.readlines()

    data = [row.split('\t') for row in data]
    data = [(row[1], row[0]) for row in data]

    resultado = dict()
    for key , value in data:
        key = int(key)
        if key in resultado.keys():
            resultado[key].append(value)
        else:
            resultado[key] = [value]

    tupla = [(key, value) for key, value in resultado.items()]
    tupla = sorted(tupla, key=itemgetter(0))

    return tupla


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    from operator import itemgetter

    with open('data.csv', 'r') as file:
        data = file.readlines()

    data = [row.split('\t') for row in data]
    data = [(row[1], row[0]) for row in data]

    resultado = dict()
    for key , value in data:
        key = int(key)
        if key in resultado.keys():
            resultado[key].append(value)
        else:
            resultado[key] = [value]

    tupla = [(key, sorted(list(set(value)))) for key, value in resultado.items()]
    tupla = sorted(tupla, key=itemgetter(0))

    return tupla


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    from operator import itemgetter

    with open('data.csv', 'r') as f:
        data = f.readlines()

    data =[row.split('\t') for row in data]
    data =[row[4].strip('\n') for row in data]
    data =[row.split(',') for row in data]
    
    duplas = list()

    for row in data:
        for dupla in row:
            key, value = dupla.split(':')
            duplas.append(key)        


    tuplas = {row:duplas.count(row) for row in duplas}
    tuplas = sorted(tuplas.items())
    
    res = dict(tuplas)

    return res



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    from operator import itemgetter

    with open('data.csv', 'r') as f:
        data = f.readlines()

    data = [row.split('\t') for row in data]
    data = [(row[0],len(row[3].split(',')),len(row[4].split(','))) for row in data]

    return data



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

    with open('data.csv', 'r') as f:
        data = f.readlines()

    data = [row.split('\t') for row in data]
    data = [(row[1], row[3]) for row in data]

    resultado = dict()
    for key, value in data:
        value = value.split(',')
        for letter in value:
            key = int(key)
            if letter in resultado.keys():
                resultado[letter] += key
            else:
                resultado[letter] = key

    resultado = sorted(resultado.items())
    resultado = dict(resultado)

    return resultado



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    from operator import itemgetter

    with open('data.csv', 'r') as f:
        data = f.readlines()

    data =[row.split('\t') for row in data]
    data =[(row[0], row[4].strip('\n')) for row in data]
    data =[(row1, row2.split(',')) for row1, row2 in data]
    
    tuples = dict()

    for letter, values in data:
        for duple in values:
            duple = duple.split(':')
            duple[1] = int(duple[1])
            if letter in tuples.keys():
                tuples[letter].append(duple[1])
            else:
                tuples[letter] = [duple[1]]
    
    tuples = [(key, sum(values)) for key, values in tuples.items()]
    tuples = sorted(tuples, key=itemgetter(0))
    resultado = dict(tuples)

    return resultado

print(pregunta_12())