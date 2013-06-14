#
# Exercise 1
#
g.region(rast='elevation')
v.to_rast(input='streets', type='line', output='streets', use='cat', overwrite=True)
r.mapcalc(expression="dist_cost=10./cos(slope)", overwrite=True)
r.cost(input='dist_cost', output='distance_from_streets', outdir='direction', start_rast='streets', overwrite=True, flags=['k'])

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
