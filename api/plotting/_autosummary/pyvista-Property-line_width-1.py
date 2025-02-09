# Get the default line width and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.line_width
# Expected:
## 1.0
#
prop.show_edges = True
prop.plot()
#
# Visualize a line width of ``5.0``.
#
prop.line_width = 5.0
prop.plot()
#
# Visualize a line width of ``10.0``.
#
prop.line_width = 10.0
prop.plot()
