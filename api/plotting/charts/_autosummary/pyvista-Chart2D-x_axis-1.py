# Create a 2D plot and hide the x axis.
#
import pyvista as pv
chart = pv.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.x_axis.toggle()
chart.show()
