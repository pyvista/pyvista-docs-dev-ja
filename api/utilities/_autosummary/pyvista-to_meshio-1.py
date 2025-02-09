# Convert a pyvista sphere to a ``meshio`` mesh instance.
#
import pyvista as pv
sphere = pv.Sphere()
mesh = pv.to_meshio(sphere)
