# Get the default specular color and visualize it with ``specular = 0.5`` and
# Phong shading.
#
import pyvista as pv
prop = pv.Property()
prop.specular_color
# Expected:
## Color(name='lightblue', hex='#add8e6ff', opacity=255)
#
prop.specular = 0.5
prop.interpolation = 'phong'
prop.plot()
#
# Visualize red specular color.
#
prop.specular_color = 'red'
prop.plot()
#
# Visualize white specular color.
#
prop.specular_color = 'white'
prop.plot()
