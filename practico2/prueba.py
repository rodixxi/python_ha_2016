#!/usr/bin/python
# -*- coding: utf-8 -*-

from practico2 import Persona, Grupo

p0 = Persona("juan", 18)
p01 = Persona("juan", 18)
p1 = Persona("tito", 34)
p2 = Persona("carlos", 36)
p3 = Persona("jorge", 25)

g0 = p0 + p1
print g0

print p0 == p01
print p0 != p01
print p0 == p1
print p0 != p1

g1 = g0 + p2
print g1

g2 = g1 - p2
print g2

g3 = p2 + p3
print g3

g4 = g2 + g3
print g4

g5 = g4 - g2
print g2

g6 = g5 - g3
print g6

for persona in g4:
    print persona
for persona in g2:
    print persona
for persona in g5:
    print persona
for persona in g6:
    print persona

print len(g4)
print len(g5)
print len(g6)

if g5:
    print len(g5)
if g6:
    print len(g6)

print p0 in g0
print p2 in g0
print p3 in g4

print g4.edad_promedio()
print g0.edad_promedio()
print g6.edad_promedio()


