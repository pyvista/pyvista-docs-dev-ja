# Set anisotropy to 0.1
#
import pyvista as pv
prop = pv.Property()
prop.interpolation = 'pbr'
prop.anisotropy
# Expected:
## 0.1
