# Create a 2D chart with a thick, dashed red border.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
chart.border_color = 'r'
chart.border_width = 5
chart.border_style = '--'
chart.show(interactive=False)
