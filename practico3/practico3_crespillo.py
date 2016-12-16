#!/usr/bin/python
# -*- coding: utf-8 -*-


def concurrent(func):
    def wrapper(*args, **kwargs):
        import threading

        class Promice(threading.Thread):

            def __init__(self, func, *args, **kwargs):
                threading.Thread.__init__(self)
                self.func = func
                self.k = args
                self.kw = kwargs

            def run(self):
                self.func = self.func(*self.k, **self.kw)

            def get_result(self):
                if self.is_alive():
                    raise RuntimeError("{} still running!".format(
                        self.name))
                self.join()
                return self.func

        b = Promice(func, *args, **kwargs)
        b.start()
        return b
    return wrapper


def jsonparams(func):
    import json

    def func_wraper(*args, **kwargs):
        data = json.loads(*args, **kwargs)
        if isinstance(data, list):
            return func(*data)
        if isinstance(data, dict):
            return func(**data)
    return func_wraper
