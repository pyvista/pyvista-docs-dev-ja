# Read in an example jpg map file as a texture.
#
from pathlib import Path
import pyvista as pv
from pyvista import examples
Path(examples.mapfile).name
# Expected:
## '2k_earth_daymap.jpg'
texture = pv.read_texture(examples.mapfile)
type(texture)
# Expected:
## <class 'pyvista.plotting.texture.Texture'>
