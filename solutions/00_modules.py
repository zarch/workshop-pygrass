#
# Exercise 2
#
from grass.pygrass.modules import general as g
import subprocess as sub
gregion = g.region


def get_region():
    gregion(flags='p', stdout_=sub.PIPE)
    reg = {}
    for row in gregion.outputs.stdout.splitlines():
        key, value = row.split(':')
        reg[key.strip()] = value.strip()
    return reg

get_region()
