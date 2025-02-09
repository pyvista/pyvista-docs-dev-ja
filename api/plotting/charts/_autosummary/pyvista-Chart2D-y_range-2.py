import pyvista as pv
chart = pv.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.x_range = [-2, 2]
chart.y_range = [0, 5]
chart.show()
