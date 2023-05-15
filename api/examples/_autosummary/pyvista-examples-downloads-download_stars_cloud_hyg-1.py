# Download and plot a point cloud of stars within 3,000 light years. Stars
# are colored according to their RGBA colors.
#
import numpy as np
from pyvista import examples
stars = examples.download_stars_cloud_hyg()
stars.plot(
    style='points_gaussian',
    background='k',
    point_size=0.5,
    scalars='_rgba',
    render_points_as_spheres=False,
    zoom=3.0,
)
#
stars
# Expected:
## PolyData (...)
##   N Cells:    107857
##   N Points:   107857
##   N Strips:   0
##   X Bounds:   -9.755e+02, 9.774e+02
##   Y Bounds:   -9.620e+02, 9.662e+02
##   Z Bounds:   -9.788e+02, 9.702e+02
##   N Arrays:   3
#
# See the :ref:`plotting_point_clouds` for more details on how to plot point
