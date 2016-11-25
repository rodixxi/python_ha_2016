#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Strings"""


def facturas(nro):
    """
    Dado una número de facturas, implementar una función que devuleva el string
    ‘Cantidad de facturas: <nro> ‘ donde nro es el número que se pasa como
    argumento. Si las facturas son mas de 12, se tiene que devolver
    ‘Cantidad de facturas: muchas’.
    """
    cantidad = nro
    if cantidad >= 12:
        cantidad = "muchas"
    return "Cantidad de facturas: " + str(cantidad)


def ambos(s):
    """
    Dado un string s, implementar la función ambos que devuelve un string
    construido con los dos primeros y dos últimos caracteres. Por ejemplo,
    aplicar ambos a ‘primavera’ devuelve ‘prra’. Si s posee menos de dos
    caracteres, el resultado es el string vacío.
    """
    cadena = s
    if len(s) < 2:
        cadena = ""
    else:
        cadena = s[:2] + s[-2:]
    return cadena


def fix(s):
    """
    Dado un string s, implementar una función fix que reemplaza todas las
    ocurrencias del primer caracter por ‘*’ a excepción de la primera
    ocurrencia. Por ejemplo evaluar fix a la palabra ‘burbuja’ devuelve
    ‘bur*uja’. Ayuda, estudiar la función replace.
    """
    capital = s[:1]
    cadena = s[1:]
    return capital + cadena.replace(capital, "*", 1)


def mezclar(a, b):
    """
    Dados dos strings a y b, implementar la función mezclar que devuelve el
    string a y b separados por un espacio, excepto las primeros caracteres de
    cada string que son intercambiados. Por ejemplo, mezclar(‘mix’, ‘pod’)
    devuelve ‘pix mod’.
    """
    separador = " "
    cadena1 = b[:1] + a[1:]
    cadena2 = a[:1] + b[1:]
    return separador.join((cadena1, cadena2))


"""Listas"""


def macheos(args):  # No funciona
    """
    Implementar la función macheos que dada una lista de strings devuelve un
    número representando la cantidad de strings que tienen más de dos
    caracteres y cuyos últimos dos strings son iguales.
    Nota: python no posee operador ++ pero += funciona.
    """
    h = args[:1]
    t = args[1:]
    otra = []
    val = 0
    for p in h:
        if len(p) > 2:
            for s in t:
                if s.endswith(p[-2:]):
                    val += 1
                else:
                    otra.append(s)
        val += macheos(otra)
    return val


def front_x(lista):
    """
    Dada una lista de strings, implementar la funcion front_x que devuelve una
    lista ordenada exceptuando las palabras que comiencen con x, las cuales
    deben ir al principio. Por ejemplo,
    ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] devuelve
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    lista_a = lista
    lista_x = []
    for i, s in enumerate(lista_a):
        if s.startswith('x'):
            lista_x.append(s)
            lista_a.pop(i)
    lista_a.sort()
    lista_x.sort()
    lista_x.extend(lista_a)
    return lista_x


def sort_last(tupla):  # FALTA
    """
    Dada una lista de tuplas no vacias, implementar la funcion sort_last que
    devuelve una lista con las tuplas ordenadas de forma incremental según el
    último elemento de la tupla. Ejemplo: aplicar sort_last a
    [(1, 7), (1, 3), (3, 4, 5), (2, 2)] devuelve
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    pass


def tabla_de_multiplicar(nro):
    """
    Implementar la función tablas que dado un argumento nro, devuelve la tabla
    de multiplicar de nro del 1 al 10.
    """
    var = [nro * (x + 1) for x in xrange(10)]
    return var


"""Diccionarios"""


def mapeo(cadena):  # VER SI SE PUEDE ORDENAR POR VALOR
    """
    Implementar la función mapeo que toma un string y devuelve un diccionario
    con cada caracter como clave y la posición del caracter como valor.
    Ejemplo, evaluar mapeo a ‘cosa’ devuelve
    {‘c’: 0, ‘o’:1, ‘s’:2, ‘a’: 3}
    """
    dic = {}
    for i, s in enumerate(cadena):
        dic[s] = i
    return dic


def busqueda_reversa(dic, nro):
    """
    Implementar la función busqueda_reversa que dado un diccionario y un objeto
    cualquiera, permita buscar por valores de diccionarios en vez de claves.
    Ejemplo:
    d = {‘c’: 0, ‘o’:1, ‘s’:2, ‘a’: 3}
    busqueda_reversa(d, 3)
    ’a’
    """
    for name, value in dic.iteritems():
        if value == nro:
            return name


""" Tipos Combinados """


def invitados(dic):  # NO FUNCIONA
    """Imaginen que poseemos un diccionario de la forma nombre​ -> estado​
    (clave -> valor), el estado representa si la persona cuyo nombre es nombre​
    irá o no a tu cumpleaños, porejemplo:
    invitados = {"María": "Asistirá", "Luis": "Asistirá",
    "Ángel": "No asistirá", "Pedro": "Asistirá", "Carla": "No asistirá"}
    Implementar la función invitados que devuelve solo aquellas personas que
    asistirán al cumpleaños.
    """
    dic_aux = dic
    for name, estado in dic_aux.iteritems():
        if estado == "No asistira":
            del dic_aux[name]
    return dic_aux


def justificar(s):  # FALTA
    """
    Dado un string implementar la función justificar que fija la longitud de
    cada línea en 80 caracteres y justifica cada línea.

    """
    pass


""" OOP """


class Puerta(object):  # Ingresar combinacion por numero y cambiar aributos a
    #  privado
    """
    Un cerrojo con combinación tiene las siguientes propiedades básicas:
    la combinación (una secuencia de tres números); el cerrojo se puede abrir
    proporcionando la combinación; y la combinación se puede cambiar,
    pero solamente por alguien que conoce la combinación actual.
    Diseñe una clase con métodos abrir, cerrar y cambiar_combinacion, y
    atributos para almacenar la combinación y el estado de la puerta, cerrada o
    abierta. La combinación debería asignarse en el constructor.
    """

    def __init__(self, combinacion):
        self.combinacion = combinacion
        self.estado = "Abierta"

    def cerrar(self):
        self.estado = "Cerrada"

    def abrir(self):
        self.estado = "Abierta"

    def cambiar_combinacion(self, comb_actual, comb_nueva):
        if self.combinacion == comb_actual:
            self.combinacion = comb_nueva


"""Jerarquia de Clases"""  # MEJOR IMPLEMENTACION
"""
Establezca una jerarquía de clases que represente a los estudiantes de una
universidad sabiendo que todos los estudiantes se caracterizan por un nombre y
un número. Hay varios tipos de estudiantes: los estudiantes ocasionales, sean de
cursos de verano o de cursos específicos (se matriculan de un curso determinado)
, los que cursan solo una tecnicatura, licenciatura. Además, la universidad
imparte cursos de especialización gratuitos para sus empleados.
"""


class Curso(object):
    """Un curso"""

    def __init__(self, nombre):
        self.nombre = nombre


class CursoVerano(Curso):
    """Un Curso de Verano"""

    def __init__(self, nombre):
        super(CursoVerano, self).__init__(nombre)


class CursoGratuito(Curso):
    """Un Curso Gratuito"""

    def __init__(self, nombre):
        super(CursoGratuito, self).__init__(nombre)


class Persona(object):
    """Una Persona"""

    def __init__(self, nombre):
        self.nombre = nombre


class Alumno(Persona):
    """Un Alumno"""

    def __init__(self, nombre, legajo):
        super(Alumno, self).__init__(nombre)
        self.legajo = legajo


class AlumnoTemporal(Alumno):
    """Un Alumno Temporal"""

    def __init__(self, nombre, legajo):
        super(AlumnoTemporal, self).__init__(nombre, legajo)
        self.cursos = []

    def agregar_curso(self, CursoVerano):
        self.cursos.append(CursoVerano)


class Empleado(Persona):
    """Un Empleado"""

    def __init__(self, nombre):
        super(Empleado, self).__init__(nombre)
        self.cursos = []

    def agregar_curso(self, CursoGratuito):
        self.cursos.append(CursoGratuito)

"""
Triangulo
Escriba una clase, triángulo, que represente un triángulo. La clase debe incluir
los siguientes métodos que devuelven un valor lógico indicando el tipo del
triángulo:
es_rectangulo (para triángulos rectángulos)
es_escaleno (todos los lados distintos)
es_isosceles (dos lados iguales y el otro distinto)
es_equilatero (los tres lados iguales)
"""

"""
Una Persona
Construya una estructura de clases que represente una serie de personas
caracterizadas por el nombre (compuesto de nombre de pila y dos apellidos) y el
número del DNI. Debe ser posible imprimir los datos completos de una persona y
devolver el nombre o el DNI independientemente.
"""
"""
Genelogia
Modifique el ejemplo anterior para poder construir un árbol genealógico donde se
establezca dinámicamente un vínculo que indique qué persona es el padre y cual
la madre de una persona dada.
"""