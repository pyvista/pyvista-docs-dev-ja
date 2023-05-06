# Create a bar plot.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.bar([1, 2, 3], [2, 1, 3])
chart.show()
#
# Update the bar sizes.
#
plot.update([1, 2, 3], [3, 1, 2])
chart.show()
