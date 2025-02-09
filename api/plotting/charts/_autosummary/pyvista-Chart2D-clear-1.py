# Create a 2D chart with multiple line and scatter plot.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
_ = chart.plot([0, 1, 2], [2, 1, 3], 'o-b')
_ = chart.plot([-2, -1, 0], [3, 1, 2], 'd-r')
chart.show()
#
#    Remove all scatter plots from the chart.
#
chart.clear('scatter')
chart.show()
