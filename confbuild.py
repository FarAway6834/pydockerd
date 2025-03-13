from jsontool import *

for i, j in getJ('conf.json').items(): setJ(i, j)