# Set interpolation to physically based rendering.
#
import pyvista as pv
prop = pv.Property()
prop.interpolation = 'pbr'
prop.interpolation
# Expected:
## <InterpolationType.PBR: 3>
#
# Visualize default flat shading.
#
prop.interpolation = 'Flat'
prop.plot()
#
# Visualize gouraud shading.
#
prop.interpolation = 'Gouraud'
prop.plot()
#
# Visualize phong shading.
#
prop.interpolation = 'Phong'
prop.plot()
#
# Visualize physically based rendering.
#
prop.interpolation = 'Physically based rendering'
prop.plot()
