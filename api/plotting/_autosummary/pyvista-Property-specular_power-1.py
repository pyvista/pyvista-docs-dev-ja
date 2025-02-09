# Get the default specular power value and visualize it with ``specular = 1.0``
# and Phong shading.
#
import pyvista as pv
prop = pv.Property()
prop.specular_power
# Expected:
## 100.0
prop.specular = 1.0
prop.interpolation = 'phong'
prop.plot()
#
# Visualize specular power at ``50.0``.
#
prop.specular_power = 50.0
prop.plot()
#
# Visualize specular power at ``10.0``.
#
prop.specular_power = 10.0
prop.plot()
