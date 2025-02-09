import pyvista as pv
chart = pv.Chart2D()
plot = chart.stack([0, 1, 2], [[2, 1, 3], [1, 2, 1]])
chart.show()
#
# Update the stack sizes.
#
plot.update([0, 1, 2], [[3, 1, 2], [0, 3, 1]])
chart.show()
