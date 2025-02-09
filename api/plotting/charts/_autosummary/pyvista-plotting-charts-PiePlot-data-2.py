import pyvista as pv
chart = pv.ChartPie([1, 2, 3])
chart.plot.data
# Expected:
## pyvista_ndarray([1, 2, 3])
chart.show()
