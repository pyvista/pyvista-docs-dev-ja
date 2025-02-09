# Get the default edge visibility and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.show_edges
# Expected:
## False
prop.plot()
#
# Visualize setting the visibility to ``True``.
#
prop.show_edges = True
prop.plot()
