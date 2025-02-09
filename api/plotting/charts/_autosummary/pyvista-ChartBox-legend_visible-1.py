# Create a boxplot chart with custom labels.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.plot.label = "Data label"
chart.show()
#
#    Hide the legend.
#
chart.legend_visible = False
chart.show()
