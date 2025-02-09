# Get the default lighting and visualize it
#
import pyvista as pv
prop = pv.Property()
prop.lighting
# Expected:
## True
prop.plot()
#
# Visualize disabled lighting.
#
prop.lighting = False
prop.plot()
