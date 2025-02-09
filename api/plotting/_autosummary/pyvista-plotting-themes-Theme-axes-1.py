# Set the x-axis color to black.
#
import pyvista as pv
pv.global_theme.axes.x_color = 'black'
#
# Show the axes orientation widget by default.
#
pv.global_theme.axes.show = True
#
# Use the :func:`axes orientation box <pyvista.create_axes_orientation_box>` as the orientation widget.
#
pv.global_theme.axes.box = True
