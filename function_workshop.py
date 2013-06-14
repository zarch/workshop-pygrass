# define a funcion to show raster map
from IPython.core.display import Image
from grass.pygrass.modules.shortcuts import raster
def show(mapname):
    imgname = mapname + '.png'
    raster.out_png(input=mapname, output=imgname, overwrite=True)
    return Image(filename=imgname)