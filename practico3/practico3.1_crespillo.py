#!/usr/bin/python
# -*- coding: utf-8 -*-


def concurrent(func):
    import threading

    class Promice(threading.Thread):

        def __init__(self, *args, **kwargs):
            threading.Thread.__init__(self)
            self.func = func(*args, **kwargs)
            

        def run(self):
            return

        def get_result(self):
            if self.isAlive():
                raise Exception("Se lo llamo antes de los 10 segundos")
            else:
                self.join()

    return Promice


import time
import threading

print "1Number of threads active", threading.activeCount()


@concurrent
def function(a, b):
    # esta funcion duerme aprox 10 segundos ante de terminar
    time.sleep(1)
    return a + b


promise = function(1, 2)

time.sleep(3)

# falla si se llama antes de ~10 segundos o devueltve 3
promise.get_result()
print "3Number of threads active", threading.activeCount()
