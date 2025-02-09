import pyvista as pv
chart = pv.ChartPie([5, 4, 3, 2, 1])
chart.show()
#
# Hide it.
#
chart.visible = False
chart.show()
