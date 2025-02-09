# Get the default x-axis color
#
import pyvista as pv
pv.global_theme.axes.x_color
# Expected:
## Color(name='tomato', hex='#ff6347ff', opacity=255)
#
# Change the default color.
#
pv.global_theme.axes.x_color = 'red'
