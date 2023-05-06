import pyvista as pv
prop = pv.Property()
prop.diffuse = 0.2
prop.diffuse
# Expected:
## 0.2
#
# Visualize default diffuse light.
#
prop.diffuse = 1.0
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
