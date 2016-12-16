#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import datetime


def valid_date(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        msg = "No es una fecha valida: {0}.".format(s)
        raise argparse.ArgumentError(msg)


parser = argparse.ArgumentParser(description="Diferecia entre dos fechas")

parser.add_argument('--from',
                    help="The FROM Date - format YYYY-MM-DDTHH:MM:SS.mmmmmm ",
                    dest='date',
                    action='append',
                    required=True,
                    type=valid_date)

parser.add_argument('--to',
                    help="The TO - format YYYY-MM-DDTHH:MM:SS.mmmmmm ",
                    dest='date',
                    action='append',
                    required=True,
                    type=valid_date)

args = parser.parse_args()

diff = (args.date[1] - args.date[0]).total_seconds()

print "Diferencia: {0} secs.".format(diff)
