import pyvista as pv
prop = pv.Property()
prop.show_edges = True
prop.show_edges
# Expected:
## True
#
# Visualize default edge visibility of ``False``.
#
prop.show_edges = False
prop.plot()
#
# Visualize edge visibility of ``True``.
#
prop.show_edges = True
prop.plot()
