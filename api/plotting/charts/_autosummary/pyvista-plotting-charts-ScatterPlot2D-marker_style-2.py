import pyvista as pv
chart = pv.Chart2D()
plot = chart.scatter([0, 1, 2, 3, 4], [2, 1, 3, 4, 2])
chart.show()
#
# Change the marker style.
#
plot.marker_style = 'd'
chart.show()
