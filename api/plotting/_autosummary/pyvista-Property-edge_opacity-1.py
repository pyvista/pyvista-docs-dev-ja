# Set edge opacity to ``0.5``.
#
import pyvista as pv
prop = pv.Property()
prop.show_edges = True
prop.edge_opacity = 0.5
prop.edge_opacity
# Expected:
## 0.5
#
# Visualize default edge opacity of ``1.0``.
#
prop.edge_opacity = 1.0
prop.plot()
#
# Visualize edge opacity of ``0.1``.
#
prop.edge_opacity = 0.1
prop.plot()
