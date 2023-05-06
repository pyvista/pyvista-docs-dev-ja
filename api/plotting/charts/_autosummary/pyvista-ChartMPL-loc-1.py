# Create a half-sized matplotlib chart centered in the middle of the
# renderer.
#
import pyvista
chart = pyvista.ChartMPL()
plots = chart.figure.axes[0].plot([0, 1, 2], [2, 1, 3])
chart.size = (0.5, 0.5)
chart.loc = (0.25, 0.25)
chart.show()
