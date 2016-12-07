#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools


class Persona(object):
    """Una Persona"""

    def __init__(self, nombre, edad):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe se un string!")
        else:
            self._nombre = nombre
        if not isinstance(edad, int):
            raise TypeError("La edad debe es un int!")
        else:
            self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    def __iter__(self):
        return self

    def __add__(self, other):
        if not isinstance(other, Persona):
            raise TypeError("Debe sumar una Persona")
        else:
            return Grupo(list(itertools.chain([self], [other])))

    def __repr__(self):
        return "<Persona '{}'>".format(self.nombre)

    def __eq__(self, other):
        if not isinstance(other, Persona):
            return TypeError("Debe comparar contra una Persona")
        else:
            if self.nombre == other.nombre and self.edad == other.edad:
                return True
            else:
                return False

    def __ne__(self, other):
        return not self == other


class Grupo(object):
    """Un Grupo"""

    def __init__(self, group):
        for persona in group:
            assert isinstance(persona, Persona)
        self.grupo = frozenset(group)

    def __add__(self, other):
        if isinstance(other, Persona):
            return Grupo(list(itertools.chain(list(self.grupo), [other])))
        if isinstance(other, Grupo):
            return Grupo(list(self.grupo) + list(other.grupo - self.grupo))

    def __sub__(self, other):
        if isinstance(other, Persona):
            return Grupo(list(itertools.ifilterfalse(lambda x: x == other,
                         list(self.grupo))))
        if isinstance(other, Grupo):
            return Grupo(list(self.grupo - other.grupo))

    def __iter__(self):
        for persona in self.grupo:
            yield persona

    def __len__(self):
        return len(self.grupo)

    def __nonzero__(self):
        if len(self) > 0:
            return True
        else:
            return False

    def __repr__(self):
        return "<Grupo '{} personas'>".format(len(self.grupo))

    def edad_promedio(self):
        if len(self) > 0:
            acum = 0
            for index, persona in enumerate(self.grupo):
                acum += persona.edad
                cont = index + 1
            return acum/cont
        else:
            raise EmptyGroupError()


class EmptyGroupError(ValueError):
    def __init__(self):
        super(EmptyGroupError, self).__init__("grupo vacio")


