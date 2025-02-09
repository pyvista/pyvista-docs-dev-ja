import pyvista as pv
chart = pv.ChartPie([4, 3, 2, 1])
plot = chart.plot
plot.line_style = '-'  # Make sure all lines are visible
plot.line_width = 10
chart.show()
