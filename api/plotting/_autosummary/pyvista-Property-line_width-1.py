# Change the line width to ``10``.
#
import pyvista as pv
prop = pv.Property()
prop.line_width = 10
prop.line_width
# Expected:
## 10.0
#
# Visualize the default line width.
#
prop.line_width = 1.0
prop.show_edges = True
prop.plot()
#
# Visualize with a line width of 5.0
#
prop.line_width = 5.0
prop.plot()
