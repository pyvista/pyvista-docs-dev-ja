# Get the default edge opacity and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.edge_opacity
# Expected:
## 1.0
prop.show_edges = True
prop.plot()
#
# Visualize an edge opacity of ``0.75``.
#
prop.edge_opacity = 0.75
prop.plot()
#
# Visualize wn edge opacity of ``0.25``.
#
prop.edge_opacity = 0.25
prop.plot()
