import pyvista as pv
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.show()
#
# Hide it.
#
chart.visible = False
chart.show()
