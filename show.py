# define a funcion to show raster map
from IPython.core.display import Image
from grass.pygrass.modules.shortcuts import display


def show(mapname, type='rast', start='png', output='view.png',
         select=None, width=None, height=None, resolution=None, bgcolor=None,
         overwrite=True, *args, **kwargs):
    """Return an instance of IPython Image.

    Parameters
    -----------

    mapname : Nname of the map.
    type: map type ('rast', 'vect')

    start, output, select, width, height, resolution, bgcolor, overwrite
    are parameters of d.mon module.
    *args and **kwargs are parameters of d.rast or d.vect depend from the type.
    """
    display.mon(start=start, output=output, select=select,
                width=width, height=height, resolution=resolution,
                bgcolor=bgcolor, overwrite=overwrite)
    getattr(display, type)(map=mapname, *args, **kwargs)
    display.mon(stop=start)
    return Image(filename=output)

