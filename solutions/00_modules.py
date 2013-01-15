#
# Exercise 2
#
from grass.pygrass.modules import general as g
gregion = g.region

def get_region():
    gregion(flags='p', stdout_=PIPE)
    reg = {}
    for row in gregion.stdout.splitlines():
        key, value = row.split(':')
        reg[key.strip()] = value.strip()
    return reg

get_region()
