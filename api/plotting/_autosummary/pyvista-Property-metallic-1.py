# Get the default metallic value and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.interpolation = 'pbr'  # required
prop.metallic
# Expected:
## 0.0
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
