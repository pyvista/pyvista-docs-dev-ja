# Generate a mesh with quadrilateral faces.
#
import pyvista as pv
plane = pv.Plane()
plane.point_data.clear()
plane.plot(show_edges=True, line_width=5)
#
# Convert it to an all triangle mesh.
#
mesh = plane.triangulate()
mesh.plot(show_edges=True, line_width=5)
