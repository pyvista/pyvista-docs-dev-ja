# Create a 2D chart with a line and scatter plot.
#
import pyvista
chart = pyvista.Chart2D()
scatter_plot, line_plot = chart.plot([0, 1, 2], [2, 1, 3], "o-")
chart.show()
#
# Retrieve all plots in the chart.
#
plots = [*chart.plots()]
scatter_plot in plots and line_plot in plots
# Expected:
## True
#
# Retrieve all line plots in the chart.
#
line_plots = [*chart.plots("line")]
line_plot == line_plots[0]
# Expected:
## True
