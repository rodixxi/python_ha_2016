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


def macheos(lista):
    """
    Implementar la función macheos que dada una lista de strings devuelve un
    número representando la cantidad de strings que tienen más de dos
    caracteres y cuyos últimos dos strings son iguales.
    Nota: python no posee operador ++ pero += funciona.
    """
    cantidad = len([s for s in lista if len(s) > 2 and s[-2:-1] == s[-1:]])
    return cantidad


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


def sort_last(tuple1):
    """
    Dada una lista de tuplas no vacias, implementar la funcion sort_last que
    devuelve una lista con las tuplas ordenadas de forma incremental según el
    último elemento de la tupla. Ejemplo: aplicar sort_last a
    [(1, 7), (1, 3), (3, 4, 5), (2, 2)] devuelve
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    sorted_tuple = sorted(tuple1, key=lambda x: x[-1])
    return sorted_tuple


def tabla_de_multiplicar(nro):
    """
    Implementar la función tablas que dado un argumento nro, devuelve la tabla
    de multiplicar de nro del 1 al 10.
    """
    var = [str(nro) + "*" + str(x+1) + "=" + str(nro * (x + 1)) for x in
           xrange(10)]
    return var


"""Diccionarios"""


def mapeo(cadena):
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


def lista_invitados(dic):
    """Imaginen que poseemos un diccionario de la forma nombre​ -> estado​
    (clave -> valor), el estado representa si la persona cuyo nombre es nombre​
    irá o no a tu cumpleaños, porejemplo:
    invitados = {"María": "Asistirá", "Luis": "Asistirá",
    "Ángel": "No asistirá", "Pedro": "Asistirá", "Carla": "No asistirá"}
    Implementar la función invitados que devuelve solo aquellas personas que
    asistirán al cumpleaños.
    """
    asistentes = []
    for name, estado in dic.iteritems():
        if estado == "Asistirá":
            asistentes.append(name)
    return asistentes


def justificar(text):
    """
    Dado un string implementar la función justificar que fija la longitud de
    cada línea en 80 caracteres y justifica cada línea.
    """
    line_len = 80
    text_len = len(text)
    text_clean = [text[i:i+line_len] for i in xrange(0, text_len, line_len)]
    return text_clean


""" OOP """


class Puerta(object):
    """
    Un cerrojo con combinación tiene las siguientes propiedades básicas:
    la combinación (una secuencia de tres números); el cerrojo se puede abrir
    proporcionando la combinación; y la combinación se puede cambiar,
    pero solamente por alguien que conoce la combinación actual.
    Diseñe una clase con métodos abrir, cerrar y cambiar_combinacion, y
    atributos para almacenar la combinación y el estado de la puerta, cerrada o
    abierta. La combinación debería asignarse en el constructor.
    """

    def __init__(self, c1, c2, c3):
        clave = [c1, c2, c3]
        self._combinacion = clave
        self._estado = "Abierta"

    def cerrar(self):
        self._estado = "Cerrada"

    def abrir(self):
        self._estado = "Abierta"

    def cambiar_combinacion(self, c1, c2, c3, n1, n2, n3):
        comb_actual = [c1, c2, c3]
        comb_nueva = [n1, n2, n3]
        if self._combinacion == comb_actual:
            self._combinacion = comb_nueva


"""
Establezca una jerarquía de clases que represente a los estudiantes de una
universidad sabiendo que todos los estudiantes se caracterizan por un nombre y
un número. Hay varios tipos de estudiantes: los estudiantes ocasionales, sean
de cursos de verano o de cursos específicos (se matriculan de un curso
determinado), los que cursan solo una tecnicatura, licenciatura. Además, la
universidad imparte cursos de especialización gratuitos para sus empleados.
"""


class Curso(object):
    """Un curso"""

    def __init__(self, nombre):
        self.nombre = nombre


class CursoOcasional(Curso):
    """Un Curso Temporal"""

    def __init__(self, nombre):
        super(CursoOcasional, self).__init__(nombre)


class CursoVerano(CursoOcasional):
    """Un Curso de Verano"""

    def __init__(self, nombre):
        super(CursoVerano, self).__init__(nombre)


class CursoEspecifico(CursoOcasional):
    """Un Curso Especifico"""

    def __init__(self, nombre):
        super(CursoEspecifico, self).__init__(nombre)


class CursoGratuito(Curso):
    """Un Curso Gratuito"""

    def __init__(self, nombre):
        super(CursoGratuito, self).__init__(nombre)


class Carrera(object):
    """Una Carreara"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_curso(self, curso):
        if isinstance(curso, Curso):
            self.cursos.append(curso)
        else:
            print "Esto no es un curso"

    def eliminar_curso(self, curso):
        if isinstance(curso, Curso):
            self.cursos.remove(curso)
        else:
            print "Esto no es un curso"


class Tecnicatura(Carrera):
    """Una Tecnicatira"""

    def __init__(self, nombre):
        super(Tecnicatura, self).__init__(nombre)


class Licenciatura(Carrera):
    """Una Carrera"""

    def __init__(self, nombre):
        super(Licenciatura, self).__init__(nombre)


class Persona(object):
    """Una Persona"""

    def __init__(self, nombre):
        self.nombre = nombre


class Alumno(Persona):
    """Un Alumno"""

    def __init__(self, nombre, legajo):
        super(Alumno, self).__init__(nombre)
        self.legajo = legajo


class AlumnoOcasional(Alumno):
    """Un Alumno Ocasional"""

    def __init__(self, nombre, legajo):
        super(AlumnoOcasional, self).__init__(nombre, legajo)
        self.cursos = []

    def agregar_curso(self, curso):
        if isinstance(curso, CursoOcasional):
            self.cursos.append(curso)
        else:
            print "Esto no es un curso para alumno temporal"


class AlumnoCarreara(Alumno):
    """Alumno que cursa una carrera"""

    def __init__(self, nombre, legajo):
        super(AlumnoCarreara, self).__init__(nombre, legajo)
        self.carrera = ""
        self.cursos = []

    def agregar_carrera(self, carrera):
        if isinstance(carrera, Carrera):
            self.carrera = carrera.nombre
            self.cursos = carrera.cursos
        else:
            print "Esto no es una carreara"


class Empleado(Persona):
    """Un Empleado"""

    def __init__(self, nombre):
        super(Empleado, self).__init__(nombre)
        self.cursos = []

    def agregar_curso(self, curso_gratuito):
        if isinstance(curso_gratuito, CursoGratuito):
            self.cursos.append(curso_gratuito)
        else:
            print "Esto no es un curso gratuito"


class Triangulo(object):
    """
    Triangulo
    Escriba una clase, triángulo, que represente un triángulo. La clase debe
    incluir los siguientes métodos que devuelven un valor lógico indicando el
    tipo del triángulo:
    es_rectangulo (para triángulos rectángulos)
    es_escaleno (todos los lados distintos)
    es_isosceles (dos lados iguales y el otro distinto)
    es_equilatero (los tres lados iguales)
    """

    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def es_rectangulo(self):
        if round(self.l1 ** 2) == ((self.l2 ** 2) + (self.l3 ** 2)):
            return True
        elif round(self.l2 ** 2) == ((self.l1 ** 2) + (self.l3 ** 2)):
            return True
        elif round(self.l3 ** 2) == ((self.l1 ** 2) + (self.l2 ** 2)):
            return True
        else:
            return False

    def es_escaleno(self):
        pass

    def es_isosceles(self):
        pass

    def es_equilatero(self):
        if self.l1 == self.l2 and self.l2 == self.l3:
            return True
        else:
            return False


"""
Una Persona
Construya una estructura de clases que represente una serie de personas
caracterizadas por el nombre (compuesto de nombre de pila y dos apellidos) y el
número del DNI. Debe ser posible imprimir los datos completos de una persona y
devolver el nombre o el DNI independientemente.
"""


class Persona(object):
    """Una Persona"""

    def __init__(self, nombre, apellido1, apellido2, dni):
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @property
    def dni(self):
        return self._dni

    @property
    def apellido1(self):
        return self._apellido1

    @property
    def apellido2(self):
        return self._apellido2

    def __str__(self):
        return "Nombre: " + self._nombre + \
               "\nApellidos: " + self._apellido1 + " " + self._apellido2 + \
               "\nDNI: " + str(self._dni)


"""
Genelogia
Modifique el ejemplo anterior para poder construir un árbol genealógico donde
se establezca dinámicamente un vínculo que indique qué persona es el padre y
cual la madre de una persona dada.
"""


class Arbol(object):
    """Un Arbol Genealógico"""

    def __init__(self):
        self._familia = []

    def agregar_persona(self, persona):
        if isinstance(persona, Persona):
            self._familia.append(persona)

    def buscar_padres(self, persona):
        if isinstance(persona, Persona):
            for padre in self._familia:
                if padre.dni != persona.dni:
                    if padre.apellido1 == persona.apellido1:
                        print "Su padre es:\n" + padre.__str__()
                    if padre.apellido1 == persona.apellido2:
                        print "Su madre es:\n" + padre.__str__()
