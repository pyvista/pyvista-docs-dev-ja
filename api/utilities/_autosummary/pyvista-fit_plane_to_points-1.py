# Fit a plane to a random point cloud.
#
import pyvista as pv
import numpy as np
from pyvista import examples
rng = np.random.default_rng(seed=0)
cloud = rng.random((10, 3))
cloud[:, 2] *= 0.1
plane = pv.fit_plane_to_points(cloud)
#
# Plot the point cloud and fitted plane.
#
pl = pv.Plotter()
_ = pl.add_mesh(plane, style='wireframe', line_width=4)
_ = pl.add_points(
    cloud,
    render_points_as_spheres=True,
    color='r',
    point_size=30,
)
pl.show()
#
# Fit a plane to a mesh and return its metadata. Set the plane resolution to 1
# so that the plane has no internal points or edges.
#
mesh = examples.download_shark()
plane, center, normal = pv.fit_plane_to_points(
    mesh.points, return_meta=True, resolution=1
)
#
# Plot the mesh and fitted plane.
#
pl = pv.Plotter()
_ = pl.add_mesh(plane, show_edges=True, opacity=0.25)
_ = pl.add_mesh(mesh, color='gray')
pl.camera_position = [
    (-117, 76, 235),
    (1.69, -1.38, 0),
    (0.189, 0.957, -0.22),
]
pl.show()
#
# Use the metadata with :meth:`pyvista.DataSetFilters.clip` to split the mesh into
# two.
#
first_half, second_half = mesh.clip(
    origin=center, normal=normal, return_clipped=True
)
#
# Plot the two halves of the clipped mesh.
#
pl = pv.Plotter()
_ = pl.add_mesh(first_half, color='red')
_ = pl.add_mesh(second_half, color='blue')
pl.camera_position = [
    (-143, 43, 40),
    (-8.7, -11, -14),
    (0.25, 0.92, -0.29),
]
pl.show()
#
# Note that it is pointing in the positive z-direction.
#
normal
# Expected:
## pyvista_ndarray([5.2734075e-09, 6.7008443e-08, 1.0000000e+00],
##                 dtype=float32)
#
# Use ``init_normal`` to flip the sign and make it negative instead.
#
_, _, normal = pv.fit_plane_to_points(
    mesh.points, return_meta=True, init_normal='-z'
)
normal
# Expected:
## pyvista_ndarray([-5.2734155e-09, -6.7008422e-08, -1.0000000e+00],
##                 dtype=float32)
