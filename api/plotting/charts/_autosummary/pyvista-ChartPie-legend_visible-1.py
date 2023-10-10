# Create a pie chart with custom labels.
#
import pyvista as pv
chart = pv.ChartPie([5, 4, 3, 2, 1])
chart.plot.labels = ["A", "B", "C", "D", "E"]
chart.show()
#
# Hide the legend.
#
chart.legend_visible = False
chart.show()
