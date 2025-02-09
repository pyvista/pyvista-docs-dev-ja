# Create a pie chart with a thick, dashed red border.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartPie([5, 4, 3, 2, 1])
chart.border_color = 'r'
chart.border_width = 5
chart.border_style = '--'
chart.show(interactive=False)
#
#    Set the active border color to yellow and activate the chart.
#
chart.active_border_color = 'y'
chart.show(interactive=True)
