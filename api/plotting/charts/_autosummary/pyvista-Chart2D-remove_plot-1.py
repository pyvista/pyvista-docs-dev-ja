# Create a 2D chart with a line and scatter plot.
#
import pyvista as pv
chart = pv.Chart2D()
scatter_plot, line_plot = chart.plot([0, 1, 2], [2, 1, 3], "o-")
chart.show()
#
# Remove the scatter plot from the chart.
#
chart.remove_plot(scatter_plot)
chart.show()
