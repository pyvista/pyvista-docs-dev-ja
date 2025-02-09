# Get the default ambient color and visualize it with ``ambient = 0.5``.
#
import pyvista as pv
prop = pv.Property()
prop.ambient_color
# Expected:
## Color(name='lightblue', hex='#add8e6ff', opacity=255)
#
prop.ambient = 0.5
prop.plot()
#
# Visualize red ambient color.
#
prop.ambient_color = 'red'
prop.plot()
