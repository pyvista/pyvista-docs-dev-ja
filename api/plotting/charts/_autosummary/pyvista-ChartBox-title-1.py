# Create a boxplot chart with title 'My Chart'.
#
import pyvista as pv
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.title = 'My Chart'
chart.show()
