import pyvista as pv
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.background_color = (0.5, 0.9, 0.5)
chart.show(interactive=False)
