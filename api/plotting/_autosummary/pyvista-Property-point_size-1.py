# Change the point size to ``10.0``.
#
import pyvista as pv
prop = pv.Property()
prop.point_size = 10
prop.point_size
# Expected:
## 10.0
#
# Visualize a point size of ``5.0``.
#
prop.point_size = 5.0
prop.style = 'points'
prop.plot()
#
# Visualize the a point size of ``10.0``.
#
prop.point_size = 10.0
prop.plot()
