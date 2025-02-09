# Get the default point size and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.point_size
# Expected:
## 5.0
prop.style = 'points'
prop.plot()
#
# Visualize a point size of ``10.0``.
#
prop.point_size = 10.0
prop.plot()
#
# Visualize a point size of ``50.0``.
#
prop.point_size = 50.0
prop.plot()
