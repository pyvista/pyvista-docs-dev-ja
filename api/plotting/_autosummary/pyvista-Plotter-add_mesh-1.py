# Add a sphere to the plotter and show it with a custom scalar
# bar title.
#
import pyvista as pv
sphere = pv.Sphere()
sphere['Data'] = sphere.points[:, 2]
plotter = pv.Plotter()
_ = plotter.add_mesh(
    sphere, scalar_bar_args={'title': 'Z Position'}
)
plotter.show()
#
# Plot using RGB on a single cell.  Note that since the number of
# points and the number of cells are identical, we have to pass
# ``preference='cell'``.
#
import pyvista as pv
import numpy as np
vertices = np.array(
    [
        [0, 0, 0],
        [1, 0, 0],
        [0.5, 0.667, 0],
        [0.5, 0.33, 0.667],
    ]
)
faces = np.hstack(
    [[3, 0, 1, 2], [3, 0, 3, 2], [3, 0, 1, 3], [3, 1, 2, 3]]
)
mesh = pv.PolyData(vertices, faces)
mesh.cell_data['colors'] = [
    [255, 255, 255],
    [0, 255, 0],
    [0, 0, 255],
    [255, 0, 0],
]
plotter = pv.Plotter()
_ = plotter.add_mesh(
    mesh,
    scalars='colors',
    lighting=False,
    rgb=True,
    preference='cell',
)
plotter.camera_position = 'xy'
plotter.show()
#
# Note how this varies from ``preference=='point'``.  This is
# because each point is now being individually colored, versus
# in ``preference=='point'``, each cell face is individually
# colored.
#
plotter = pv.Plotter()
_ = plotter.add_mesh(
    mesh,
    scalars='colors',
    lighting=False,
    rgb=True,
    preference='point',
)
plotter.camera_position = 'xy'
plotter.show()
#
# Plot a plane with a constant color and vary its opacity by point.
#
plane = pv.Plane()
plane.plot(
    color='b',
    opacity=np.linspace(0, 1, plane.n_points),
    show_edges=True,
)
#
# Plot the points of a sphere with Gaussian smoothing while coloring by z
# position.
#
mesh = pv.Sphere()
mesh.plot(
    scalars=mesh.points[:, 2],
    style='points_gaussian',
    opacity=0.5,
    point_size=10,
    render_points_as_spheres=False,
    show_scalar_bar=False,
)
