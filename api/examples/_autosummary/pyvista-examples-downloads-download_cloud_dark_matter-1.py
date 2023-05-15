# Download the dark matter cloud and display its representation.
#
import numpy as np
from pyvista import examples
pc = examples.download_cloud_dark_matter()
pc
# Expected:
## PointSet (...)
##   N Cells:    0
##   N Points:   32314
##   X Bounds:   7.451e+01, 7.892e+01
##   Y Bounds:   1.616e+01, 2.275e+01
##   Z Bounds:   8.900e+01, 9.319e+01
##   N Arrays:   0
#
# Plot the point cloud. Color based on the distance from the center of the
# cloud.
#
pc.plot(
    scalars=np.linalg.norm(pc.points - pc.center, axis=1),
    style='points_gaussian',
    opacity=0.5,
    point_size=1.5,
    show_scalar_bar=False,
    zoom=2,
)
