# Create a bar plot.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.bar([1, 2, 3], [[2, 1, 3], [1, 0, 2], [0, 3, 1], [3, 2, 0]])
chart.show()
#
# Modify the labels.
#
plot.labels = ["A", "B", "C", "D"]
chart.show()
