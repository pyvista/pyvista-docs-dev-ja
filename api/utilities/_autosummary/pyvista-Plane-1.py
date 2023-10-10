# Create a default plane.
#
import pyvista as pv
mesh = pv.Plane()
mesh.point_data.clear()
mesh.plot(show_edges=True)
