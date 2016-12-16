#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

from practico3_crespillo import concurrent, jsonparams


@concurrent
def function(a, b):
    # esta funcion duerme aprox 5 segundos ante de terminar
    time.sleep(5)
    return a + b


promise = function(1, 2)

# time.sleep(6)

try:
    print promise.get_result()
except RuntimeError as e:
    print e.message


@jsonparams
def function(a, b):
    return a + b


print function('{"a": 1, "b": 2}')  # retorna 3
print function('[1, 2]')  # retorna 3
