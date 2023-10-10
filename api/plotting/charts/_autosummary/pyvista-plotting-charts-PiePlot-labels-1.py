# Create a pie plot.
#
import pyvista as pv
chart = pv.ChartPie([4, 3, 2, 1])
plot = chart.plot
chart.show()
#
# Modify the labels.
#
plot.labels = ["A", "B", "C", "D"]
chart.show()
