# Get the default anisotropy and visualize it with physically-based rendering.
#
import pyvista as pv
prop = pv.Property()
prop.anisotropy
# Expected:
## 0.0
#
prop.interpolation = 'pbr'  # required
prop.plot()
