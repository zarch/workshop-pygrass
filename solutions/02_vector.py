# -*- coding: utf-8 -*-
from grass.pygrass.vector import VectorTopo
# import the random function
import random

# import the Point and Region functions?
from grass.pygrass.vector.geometry import Point
from grass.pygrass.gis.region import Region

# define a function to produce random points
def get_random_points(num):
    # inside current GRASS' region of course
    reg = Region()
    # loop over a series of numbers from 0 up to...
    for _ in xrange(0, num):
        # use the function randrange() to get both x and y random numbers
        x = random.randrange(reg.south, reg.north)
        y = random.randrange(reg.west, reg.east)
        # at the end of each loop we need to explicitly catch the pairs of x and y numbers
        # in order to produce a point
        yield Point(x, y)


def rand_vect_points(name, npoints=10, overwrite=True):
    new = VectorTopo(name)
    new.open('w', overwrite=overwrite)
    for pnt in get_random_points(npoints):
        new.write(pnt)
    new.close()
    return new
