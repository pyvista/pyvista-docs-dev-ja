# Create a pie plot.
#
import pyvista
chart = pyvista.ChartPie([4, 3, 2, 1])
plot = chart.plot
chart.show()
#
# Modify the labels.
#
plot.labels = ["A", "B", "C", "D"]
chart.show()
