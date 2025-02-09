# Get the default interpolation and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.interpolation
# Expected:
## <InterpolationType.FLAT: 0>
prop.plot()
#
# Visualize gouraud shading.
#
prop.interpolation = 'gouraud'
prop.plot()
#
# Visualize phong shading.
#
prop.interpolation = 'phong'
prop.plot()
#
# Visualize physically based rendering.
#
prop.interpolation = 'pbr'
prop.plot()
