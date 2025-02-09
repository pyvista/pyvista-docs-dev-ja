# Get the default diffuse color and visualize it with ``diffuse = 0.5``.
#
import pyvista as pv
prop = pv.Property()
prop.ambient_color
# Expected:
## Color(name='lightblue', hex='#add8e6ff', opacity=255)
#
prop.diffuse = 0.5
prop.plot()
#
# Visualize red diffuse color.
#
prop.diffuse_color = 'red'
prop.plot()
#
# Visualize white diffuse color.
#
prop.diffuse_color = 'white'
prop.plot()
