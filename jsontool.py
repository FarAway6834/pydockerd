from json import load as _l
from json import dump as _d
o = open
w, getJ = (lambda f : o(f, 'w')), (lambda f : _l(o(f))
setJ = lambda f, x : _d(x, w(f))