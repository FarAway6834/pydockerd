from jsontool import getJ

@(lambda f:f())
def load():
    for i, j in getJ('tool.json').items():
        x, y = j
        x = __import__(x)
        for z in y: x = getattr(x, z)
        global()[i] = z