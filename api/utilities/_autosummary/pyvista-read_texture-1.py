# Read in an example jpg map file as a texture.
#
import os
import pyvista as pv
from pyvista import examples
os.path.basename(examples.mapfile)
# Expected:
## '2k_earth_daymap.jpg'
texture = pv.read_texture(examples.mapfile)
type(texture)
# Expected:
## <class 'pyvista.plotting.texture.Texture'>
