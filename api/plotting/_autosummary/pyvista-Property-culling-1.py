# Enable back face culling
#
import pyvista as pv
prop = pv.Property()
prop.culling = 'back'
prop.culling
# Expected:
## 'back'
#
# Plot default culling.
#
prop.culling = 'none'
prop.plot()
#
# Plot backface culling. This looks the same as the default culling
# ``'none'`` because the forward facing faces are already obscuring the
# back faces.
#
prop.culling = 'back'
prop.plot()
#
# Plot frontface culling. Here, the forward facing faces are hidden
# entirely.
#
prop.culling = 'front'
prop.plot()
