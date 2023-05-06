# Enable rendering lines as tubes.
#
import pyvista as pv
prop = pv.Property()
prop.style = 'wireframe'
prop.line_width = 10
prop.render_lines_as_tubes = True
prop.render_lines_as_tubes
# Expected:
## True
#
# Visualize default line rendering.
#
prop.render_lines_as_tubes = False
prop.plot()
#
# Visualize rendering lines as tubes
#
prop.render_lines_as_tubes = True
prop.plot()
