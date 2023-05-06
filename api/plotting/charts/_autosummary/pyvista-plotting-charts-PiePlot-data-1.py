# Create a pie plot and display the sizes.
#
import pyvista
chart = pyvista.ChartPie([1, 2, 3])
chart.plot.data
# Expected:
## pyvista_ndarray([1, 2, 3])
chart.show()
