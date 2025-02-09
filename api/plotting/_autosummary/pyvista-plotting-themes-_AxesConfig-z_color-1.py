# Get the default z-axis color
#
import pyvista as pv
pv.global_theme.axes.z_color
# Expected:
## Color(name='blue', hex='#0000ffff', opacity=255)
#
# Change the default color.
#
pv.global_theme.axes.z_color = 'purple'
