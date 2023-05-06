import pyvista as pv
prop = pv.Property()
prop.ambient = 0.2
prop.ambient
# Expected:
## 0.2
#
# Visualize default ambient light.
#
prop.ambient = 0.0
prop.plot()
#
# Visualize ambient at ``0.5``.
#
prop.ambient = 0.5
prop.plot()
#
# Visualize ambient at ``1.0``.
#
prop.ambient = 1.0
prop.plot()
