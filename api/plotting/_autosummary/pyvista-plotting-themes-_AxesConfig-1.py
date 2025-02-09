# Show the default axes configuration values.
#
import pyvista as pv
pv.global_theme.axes.x_color
# Expected:
## Color(name='tomato', hex='#ff6347ff', opacity=255)
#
pv.global_theme.axes.y_color
# Expected:
## Color(name='seagreen', hex='#2e8b57ff', opacity=255)
#
pv.global_theme.axes.z_color
# Expected:
## Color(name='blue', hex='#0000ffff', opacity=255)
#
pv.global_theme.axes.box
# Expected:
## False
#
pv.global_theme.axes.show
# Expected:
## True
#
# Set the x-axis color to black.
#
pv.global_theme.axes.x_color = 'black'
#
# Show the axes orientation widget by default.
#
pv.global_theme.axes.show = True
#
# Use the :func:`axes orientation box <pyvista.create_axes_orientation_box>` as the orientation widget.
#
pv.global_theme.axes.box = True
