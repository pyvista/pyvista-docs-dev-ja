# Set specular power to 5.0
#
import pyvista as pv
prop = pv.Property()
prop.specular = 0.1  # enable specular
prop.specular_power = 5.0
prop.specular_power
# Expected:
## 5.0
#
# Visualize default specular power.
#
prop.specular_power = 1.0
prop.plot()
#
# Visualize specular power at ``0.1``.
#
prop.specular_power = 0.1
prop.plot()
#
# Visualize specular power at ``5.0``.
#
prop.specular_power = 5.0
prop.plot()
#
# Visualize specular power at ``128.0``.
#
prop.specular_power = 128.0
prop.plot()
