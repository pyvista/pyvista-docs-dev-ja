# Create a pie chart with a thick, dashed red border.
#
import pyvista
chart = pyvista.ChartPie([5, 4, 3, 2, 1])
chart.border_color = 'r'
chart.border_width = 5
chart.border_style = '--'
chart.show(interactive=False)
