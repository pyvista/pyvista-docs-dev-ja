# Get the default specular value and visualize it with Phong shading.
#
import pyvista as pv
prop = pv.Property()
prop.specular
# Expected:
## 0.0
prop.interpolation = 'phong'
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
