import pyvista as pv
chart = pv.ChartPie([4, 3, 2, 1])
plot = chart.plot
chart.show()
#
# Hide it.
#
plot.toggle()
chart.show()
