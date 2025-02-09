# Get the default style and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.style
# Expected:
## 'Surface'
#
prop.plot()
#
# Visualize the wireframe style.
#
prop.style = 'wireframe'
prop.plot()
#
# Visualize the points style.
#
prop.style = 'points'
prop.point_size = 5.0
prop.plot()
