# Create a boxplot chart with a green background.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.background_color = (0.5, 0.9, 0.5)
chart.show(interactive=False)
#
#    Set the active background color to blue and activate the chart.
#
chart.active_background_color = 'b'
chart.show(interactive=True)
