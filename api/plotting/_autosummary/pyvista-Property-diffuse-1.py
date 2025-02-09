# Get the default diffuse value and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.diffuse
# Expected:
## 1.0
prop.plot()
#
# Visualize diffuse at ``0.5``.
#
prop.diffuse = 0.5
prop.plot()
#
# Visualize diffuse at ``0.0``.
#
prop.diffuse = 0.0
prop.plot()
