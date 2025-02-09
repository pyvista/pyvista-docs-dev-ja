# Get the default line rendering and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.render_lines_as_tubes
# Expected:
## False
prop.show_edges = True
prop.line_width = 10
prop.edge_color = 'yellow'
prop.plot()
#
# Visualize rendering lines as tubes.
#
prop.render_lines_as_tubes = True
prop.plot()
