import pyvista as pv
chart = pv.Chart2D()
plot = chart.bar([1, 2, 3], [[2, 1, 3], [1, 0, 2], [0, 3, 1], [3, 2, 0]])
plot.colors = ['b', 'g', 'r', 'c']
chart.show()
