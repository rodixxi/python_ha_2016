#!/usr/bin/python
# -*- coding: utf-8 -*-


def jsonparams(func):
    import json

    def func_wraper(*args, **kwargs):
        data = json.loads(*args, **kwargs)
        if isinstance(data, list):
            return func(*data)
        if isinstance(data, dict):
            return func(**data)
    return func_wraper


@jsonparams
def function(a, b):
    return a * b

print function('{"a": 1, "b": 2}') # retorna 3
print function('[1, 2]') # retorna 3
