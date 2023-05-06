# First, generate 30 points on circle and plot them.
#
import pyvista as pv
points = pv.Polygon(n_sides=30).points
circle = pv.PolyData(points)
circle.plot(show_edges=True, point_size=15)
#
# Use :func:`delaunay_2d` to fill the interior of the circle.
#
filled_circle = circle.delaunay_2d()
filled_circle.plot(show_edges=True, line_width=5)
#
# Use the ``edge_source`` parameter to create a constrained delaunay
# triangulation and plot it.
#
squar = pv.Polygon(n_sides=4, radius=8, fill=False)
squar = squar.rotate_z(45, inplace=False)
circ0 = pv.Polygon(center=(2, 3, 0), n_sides=30, radius=1)
circ1 = pv.Polygon(center=(-2, -3, 0), n_sides=30, radius=1)
comb = circ0 + circ1 + squar
tess = comb.delaunay_2d(edge_source=comb)
tess.plot(cpos='xy', show_edges=True)
