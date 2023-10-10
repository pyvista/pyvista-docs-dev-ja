# Create a 2D chart.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
chart.show()
#
# Hide it.
#
chart.toggle()
chart.show()
