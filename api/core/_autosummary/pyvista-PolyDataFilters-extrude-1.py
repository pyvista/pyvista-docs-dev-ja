# Extrude a half circle arc.
#
import pyvista as pv
arc = pv.CircularArc([-1, 0, 0], [1, 0, 0], [0, 0, 0])
mesh = arc.extrude([0, 0, 1], capping=False)
mesh.plot(color='lightblue')
#
# Extrude and cap an 8 sided polygon.
#
poly = pv.Polygon(n_sides=8)
mesh = poly.extrude((0, 0, 1.5), capping=True)
mesh.plot(line_width=5, show_edges=True)
