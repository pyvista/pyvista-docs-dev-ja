import pyvista as pv
chart = pv.ChartPie([1, 2, 3, 4, 5])
chart.show()
#
# Update the pie plot (segments of equal size).
#
chart.plot.update([1, 1, 1, 1, 1])
chart.show()
