import pyvista as pv
chart = pv.ChartBox([[0, 1, 1, 2, 3, 4, 5], [0, 1, 2, 2, 3, 4, 5], [0, 1, 2, 3, 3, 4, 5], [0, 1, 2, 3, 4, 4, 5]])
plot = chart.plot
chart.show()
#
# Modify the labels.
#
plot.labels = ['A', 'B', 'C', 'D']
chart.show()
