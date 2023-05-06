# Set metallic to 0.1
#
import pyvista as pv
prop = pv.Property()
prop.interpolation = 'pbr'
prop.metallic = 0.1
prop.metallic
# Expected:
## 0.1
#
# Visualize default metallic.
#
prop.metallic = 0.0
prop.plot()
#
# Visualize metallic at ``0.5``.
#
prop.metallic = 0.5
prop.plot()
#
# Visualize metallic at ``1.0``.
#
prop.metallic = 1.0
prop.plot()
