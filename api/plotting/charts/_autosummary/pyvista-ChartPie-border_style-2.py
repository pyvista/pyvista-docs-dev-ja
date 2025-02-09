import pyvista as pv
chart = pv.ChartPie([5, 4, 3, 2, 1])
chart.border_color = 'r'
chart.border_width = 5
chart.border_style = '--'
chart.show(interactive=False)
