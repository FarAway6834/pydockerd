from tool import *
from tempfile import TemporaryDirectory as tempdir
from os.path import join as _j
from urllib.request import urlopen as _o
from re import search as _s
from os import rename as __mv__

def __wgetv__(url):
    with _o(url) as res:
        yield red.read()
        disp = res.headers.get("Content-Disposition")
        if disp:
            disp = _s(r'filename\*?=(?:UTF-8\'\')?["\']?([^"\']+)["\']?', disp)
            if disp:
                yield disp.groop(1)
    yield url.split('/')[-1]

def wget(dir, url):
    v = [x for x in __wgetv__(url)]
    fn = _j(dir, v[1])
    with open(, 'wb') as fp: fp.write(v[0])
    return fn

with tempdir() as pwd:
    from i, j in getJ('os.json').items():
        f = wget(pwd, j)
        tool[i](f)
        __mv__(f, i)