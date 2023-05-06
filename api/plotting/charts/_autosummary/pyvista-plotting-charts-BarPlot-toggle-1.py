# Create a bar plot.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.bar([1, 2, 3], [2, 1, 3])
chart.show()
#
# Hide it.
#
plot.toggle()
chart.show()
