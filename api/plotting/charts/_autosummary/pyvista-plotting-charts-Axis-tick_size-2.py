import pyvista as pv
chart = pv.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.x_axis.tick_size += 10
chart.x_axis.tick_labels_offset += 12
chart.show()
