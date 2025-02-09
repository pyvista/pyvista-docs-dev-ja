# Return the bounds across blocks.
#
import pyvista as pv
data = [
    pv.Sphere(center=(2, 0, 0)),
    pv.Cube(center=(0, 2, 0)),
    pv.Cone(),
]
blocks = pv.MultiBlock(data)
blocks.bounds
# Expected:
## BoundsTuple(x_min=-0.5, x_max=2.5, y_min=-0.5, y_max=2.5, z_min=-0.5, z_max=0.5)
