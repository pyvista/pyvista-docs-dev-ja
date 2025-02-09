# Get the default ambient value and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.ambient
# Expected:
## 0.0
#
prop.plot()
#
# Visualize ambient at ``0.25``.
#
prop.ambient = 0.25
prop.plot()
#
# Visualize ambient at ``0.75``.
#
prop.ambient = 0.75
prop.plot()
