# Set the color to blue.
#
import pyvista as pv
prop = pv.Property()
prop.color = 'b'
prop.color
# Expected:
## Color(name='blue', hex='#0000ffff', opacity=255)
#
# Visualize setting the property to blue.
#
prop.color = 'b'
prop.plot()
#
# Visualize setting the color using an RGB value.
#
prop.color = (0.5, 0.5, 0.1)
prop.plot()
