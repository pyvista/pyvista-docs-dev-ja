# Get the default color and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.color
# Expected:
## Color(name='lightblue', hex='#add8e6ff', opacity=255)
#
prop.plot()
#
# Visualize a red color.
#
prop.color = 'red'
prop.plot()
#
# Visualize an RGB color.
#
prop.color = (0.5, 0.5, 0.1)
prop.plot()
