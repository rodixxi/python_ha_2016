import argparse

FUNC = {
    "mean": lambda l: sum(l) / len(l),
    "sum": sum, "max": max
}

parser = argparse.ArgumentParser(
     description='Process some integers.')

parser.add_argument(
     'integers',
     metavar='N',
     type=float,
     nargs='+',
     help='an integer for the accumulator')

parser.add_argument(
     '--func',
     dest='func',
     type=lambda fname: FUNC[fname],
     action='store',
     required=True,
     help="Execute a function")

args = parser.parse_args()

print args.func(args.integers)


