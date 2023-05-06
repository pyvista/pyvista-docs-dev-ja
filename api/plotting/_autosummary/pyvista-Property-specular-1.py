import pyvista as pv
prop = pv.Property()
prop.specular = 0.2
prop.specular
# Expected:
## 0.2
#
# Visualize default specular light.
#
prop.specular = 0.0
prop.plot()
#
# Visualize specular at ``0.5``.
#
prop.specular = 0.5
prop.plot()
#
# Visualize specular at ``1.0``.
#
prop.specular = 1.0
prop.plot()
