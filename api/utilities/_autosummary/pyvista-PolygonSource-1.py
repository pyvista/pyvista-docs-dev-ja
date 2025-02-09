# Create an 8 sided polygon.
#
import pyvista as pv
source = pv.PolygonSource(n_sides=8)
source.output.plot(show_edges=True, line_width=5)
