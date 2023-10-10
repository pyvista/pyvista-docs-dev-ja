# Create a box with subdivision ``level=2``.
#
import pyvista as pv
mesh = pv.Box(level=2)
mesh.plot(show_edges=True)
