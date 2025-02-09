# Create a matplotlib chart.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartMPL()
plots = chart.figure.axes[0].plot([0, 1, 2], [2, 1, 3])
chart.show()
#
#    Hide it.
#
chart.toggle()
chart.show()
