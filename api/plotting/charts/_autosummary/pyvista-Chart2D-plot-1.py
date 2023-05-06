# Generate a line plot.
#
import pyvista
chart = pyvista.Chart2D()
_, line_plot = chart.plot(range(10), range(10))
chart.show()
#
# Generate a line and scatter plot.
#
chart = pyvista.Chart2D()
scatter_plot, line_plot = chart.plot(range(10), fmt='o-')
chart.show()
