import pyvista as pv
chart = pv.ChartMPL()
plots = chart.figure.axes[0].plot([0, 1, 2], [2, 1, 3])
chart.size = (0.5, 0.5)
chart.loc = (0.25, 0.25)
chart.show()
