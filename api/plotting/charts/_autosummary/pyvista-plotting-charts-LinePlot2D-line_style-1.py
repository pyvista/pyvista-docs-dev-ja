# Set a custom line style.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
plot.line_style = '-.'
chart.show()
