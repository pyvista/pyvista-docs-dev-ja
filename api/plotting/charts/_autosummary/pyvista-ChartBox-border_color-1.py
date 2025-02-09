# Create a boxplot chart with a thick, dashed red border.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.border_color = 'r'
chart.border_width = 5
chart.border_style = '--'
chart.show(interactive=False)
