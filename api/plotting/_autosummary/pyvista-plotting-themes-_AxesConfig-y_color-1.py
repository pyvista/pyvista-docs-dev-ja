# Get the default y-axis color
#
import pyvista as pv
pv.global_theme.axes.y_color
# Expected:
## Color(name='seagreen', hex='#2e8b57ff', opacity=255)
#
# Change the default color.
#
pv.global_theme.axes.y_color = 'green'
