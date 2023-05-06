# Disable lighting.
#
import pyvista as pv
prop = pv.Property()
prop.lighting = False
prop.lighting
# Expected:
## False
#
# Visualize it.
#
prop.plot()
