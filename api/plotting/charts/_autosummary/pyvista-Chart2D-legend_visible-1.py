# Create a 2D chart with custom labels.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
plot.label = "My awesome plot"
chart.show()
#
# Hide the legend.
#
chart.legend_visible = False
chart.show()
