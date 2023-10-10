# Create a default cube.
#
import pyvista as pv
mesh = pv.Cube()
mesh.plot(show_edges=True, line_width=5)
