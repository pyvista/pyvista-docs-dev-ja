# Create a 2D chart with a thick, dashed red border.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
chart.border_color = 'r'
chart.border_width = 5
chart.border_style = '--'
chart.show(interactive=False)
#
#    Set the active border color to yellow and activate the chart.
#
chart.active_border_color = 'y'
chart.show(interactive=True)
