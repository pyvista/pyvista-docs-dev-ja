# Create a matplotlib chart with a green background.
#
import pyvista as pv
chart = pv.ChartMPL()
plots = chart.figure.axes[0].plot([0, 1, 2], [2, 1, 3])
chart.background_color = (0.5, 0.9, 0.5)
chart.show(interactive=False)
