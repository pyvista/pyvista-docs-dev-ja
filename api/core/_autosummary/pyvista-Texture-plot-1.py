# Plot a simple texture.
#
from pyvista import examples
texture = examples.download_masonry_texture()
texture.plot()
#
# Plot a cubemap as a skybox.
#
cube_map = examples.download_dikhololo_night()
cube_map.plot()
