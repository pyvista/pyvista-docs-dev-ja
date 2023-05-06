# Create a pie plot with segments of increasing size.
#
import pyvista
chart = pyvista.ChartPie([1, 2, 3, 4, 5])
chart.show()
#
# Update the pie plot (segments of equal size).
#
chart.plot.update([1, 1, 1, 1, 1])
chart.show()
