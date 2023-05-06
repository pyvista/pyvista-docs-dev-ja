import pyvista as pv
cone = pv.Cone(height=2.0, radius=0.5)
plotter = pv.Plotter()
_ = plotter.add_mesh(cone)
#
# Measure x direction of cone and place ruler slightly below.
#
_ = plotter.add_ruler(
    pointa=[cone.bounds[0], cone.bounds[2] - 0.1, 0.0],
    pointb=[cone.bounds[1], cone.bounds[2] - 0.1, 0.0],
    title="X Distance",
)
#
# Measure y direction of cone and place ruler slightly to left.
# The title and labels are placed to the right of the ruler when
# traveling from ``pointa`` to ``pointb``.
#
_ = plotter.add_ruler(
    pointa=[cone.bounds[0] - 0.1, cone.bounds[3], 0.0],
    pointb=[cone.bounds[0] - 0.1, cone.bounds[2], 0.0],
    flip_range=True,
    title="Y Distance",
)
plotter.enable_parallel_projection()
plotter.view_xy()
plotter.show()
