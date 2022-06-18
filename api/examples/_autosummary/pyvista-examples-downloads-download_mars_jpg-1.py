# Download the Mars JPEG and map it to spherical coordinates on a sphere.
#
import math
import numpy
import numpy as np
from pyvista import examples
import pyvista
#
# Download the JPEGs and convert the Mars JPEG to a texture.
#
mars_jpg = examples.download_mars_jpg()
mars_tex = pyvista.read_texture(mars_jpg)
stars_jpg = examples.download_stars_jpg()
#
# Create a sphere mesh and compute the texture coordinates.
#
sphere = pyvista.Sphere(radius=1, theta_resolution=120, phi_resolution=120,
                        start_theta=270.001, end_theta=270)
sphere.active_t_coords = numpy.zeros((sphere.points.shape[0], 2))
sphere.active_t_coords[:, 0] = 0.5 + np.arctan2(-sphere.points[:, 0],
                                                sphere.points[:, 1])/(2 * math.pi)
sphere.active_t_coords[:, 1] = 0.5 + np.arcsin(sphere.points[:, 2]) / math.pi
sphere.point_data
# Expected:
## pyvista DataSetAttributes
## Association     : POINT
## Active Scalars  : None
## Active Vectors  : None
## Active Texture  : Texture Coordinates
## Active Normals  : Normals
## Contains arrays :
##     Normals                 float32    (14280, 3)           NORMALS
##     Texture Coordinates     float64    (14280, 2)           TCOORDS
#
# Plot with stars in the background.
#
pl = pyvista.Plotter()
pl.add_background_image(stars_jpg)
_ = pl.add_mesh(sphere, texture=mars_tex)
pl.show()
