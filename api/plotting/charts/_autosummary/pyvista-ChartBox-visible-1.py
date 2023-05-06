# Create a boxplot chart.
#
import pyvista
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.show()
#
# Hide it.
#
chart.visible = False
chart.show()
