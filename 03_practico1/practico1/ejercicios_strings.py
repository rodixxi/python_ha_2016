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
    cadena = s
    if len(s) < 2:
        cadena = ""
    else:
        cadena = s[:2] + s[-2:]
    return cadena


def fix(s):
    capital = s[:1]
    cadena = s[1:]
    return capital + cadena.replace(capital, "*", 1)


def mezclar(a, b):
    separador = " "
    cadena1 = b[:1] + a[1:]
    cadena2 = a[:1] + b[1:]
    return separador.join((cadena1, cadena2))


"""Listas"""


def macheos(args):
    """
    No funciona
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


def tabla_de_multiplicar(nro):
    var = [nro * (x + 1) for x in xrange(10)]
    return var


"""Diccionarios"""


def mapeo(cadena):
    dic = {}
    for i, s in enumerate(cadena):
        dic[s] = i
    return dic


def busqueda_reversa(dic, nro):
    for name, value in dic.iteritems():
        if value == nro:
            return name


"""
val = mapeo("cosa")
print val
print busqueda_reversa(val, 2)
"""


def invitados(dic):
    dic_aux = dic
    for name, estado in dic_aux.iteritems():
        if estado == "No asistira":
            del dic_aux[name]
    return  dic_aux


class Puerta(object):
    """Una puerta"""

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


"""Jerarquia de Clases"""


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


