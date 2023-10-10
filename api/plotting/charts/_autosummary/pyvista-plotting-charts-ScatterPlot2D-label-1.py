# Create a 2D scatter plot with custom label.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.scatter([0, 1, 2, 3, 4], [2, 1, 3, 4, 2])
plot.label = "My awesome plot"
chart.show()
