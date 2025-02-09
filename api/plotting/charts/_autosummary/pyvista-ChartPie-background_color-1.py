# Create a pie chart with a green background.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartPie([5, 4, 3, 2, 1])
chart.background_color = (0.5, 0.9, 0.5)
chart.show(interactive=False)
