# Create plot the masonry testure on a surface.
#
import pyvista as pv
from pyvista import examples
texture = examples.download_masonry_texture()
surf = pv.Cylinder()
surf.plot(texture=texture)
#
# .. seealso::
#
#     :ref:`Masonry Texture Dataset <masonry_texture_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`texture_example`
