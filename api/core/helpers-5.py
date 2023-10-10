# Fit a plane to a random point cloud.
#
import pyvista as pv
import numpy as np
cloud = np.random.random((10, 3))
cloud[:, 2] *= 0.1
plane, center, normal = pv.fit_plane_to_points(
    cloud, return_meta=True
)
pl = pv.Plotter()
_ = pl.add_mesh(
    plane, color='lightblue', style='wireframe', line_width=4
)
_ = pl.add_points(
    cloud,
    render_points_as_spheres=True,
    color='r',
    point_size=30,
)
pl.show()
#
# Fit a plane to a mesh.
#
import pyvista as pv
from pyvista import examples
mesh = examples.download_shark()
plane = pv.fit_plane_to_points(mesh.points)
pl = pv.Plotter()
_ = pl.add_mesh(
    plane, show_edges=True, color='lightblue', opacity=0.25
)
_ = pl.add_mesh(mesh, color='gray')
pl.camera_position = [
    (-117, 76, 235),
    (1.69, -1.38, 0),
    (0.189, 0.957, -0.22),
]
pl.show()
