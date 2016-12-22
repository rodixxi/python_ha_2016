#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import datetime
import threading
import json


# =============================================================================
# EJE 1
# =============================================================================

class Promise(threading.Thread):
    def __init__(self, target, args, kwargs):
        super(Promise, self).__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.resultado = self.target(*self.args, **self.kwargs)

    def get_result(self):
        return self.resultado


def concurrent(func):
    def inner(*args, **kwargs):
        p = Promise(func, args, kwargs)
        p.start()
        return p
    return inner


# =============================================================================
# EJE 2
# =============================================================================

def jsonparams(func):
    def inner(json_code):
        params = json.loads(json_code)
        if isinstance(params, dict):
            return func(**params)
        return func(*params)
    return inner


# =============================================================================
# EJE 3
# =============================================================================

def eje_3():

    def date(string):
        return datetime.datetime.strptime(string, "%Y-%m-%dT%H:%M:%S.%f")

    parser = argparse.ArgumentParser(description="Diferencia entre fechas")
    parser.add_argument(
        "-f", "--from", dest="from_date", help="Desde que fecha.", type=date)
    parser.add_argument(
        "-t", "--to", dest="to_date", help="Hasta que fecha", type=date)
    args = parser.parse_args()

    res = args.from_date - args.to_date

    print("Diferencia: {} secs.".format(res.total_seconds()))
