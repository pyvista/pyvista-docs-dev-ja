# Create a cube and return the bounds of the mesh.
#
import pyvista as pv
cube = pv.Cube()
cube.bounds
# Expected:
## BoundsTuple(x_min=-0.5, x_max=0.5, y_min=-0.5, y_max=0.5, z_min=-0.5, z_max=0.5)
