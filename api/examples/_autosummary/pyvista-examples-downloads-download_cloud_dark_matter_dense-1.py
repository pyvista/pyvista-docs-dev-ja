# Download the dark matter cloud and display its representation.
#
import numpy as np
from pyvista import examples
pc = examples.download_cloud_dark_matter_dense()
pc
# Expected:
## PointSet (...)
##   N Cells:    0
##   N Points:   2062256
##   X Bounds:   7.462e+01, 7.863e+01
##   Y Bounds:   1.604e+01, 2.244e+01
##   Z Bounds:   8.893e+01, 9.337e+01
##   N Arrays:   0
#
# Plot the point cloud. Color based on the distance from the center of the
# cloud.
#
pc.plot(
    scalars=np.linalg.norm(pc.points - pc.center, axis=1),
    style='points_gaussian',
    opacity=0.030,
    point_size=2.0,
    show_scalar_bar=False,
    zoom=2,
)
#
# .. seealso::
#
#     :ref:`Cloud Dark Matter Dense Dataset <cloud_dark_matter_dense_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Cloud Dark Matter Dataset <cloud_dark_matter_dataset>`
#
#     :ref:`plotting_point_clouds`
