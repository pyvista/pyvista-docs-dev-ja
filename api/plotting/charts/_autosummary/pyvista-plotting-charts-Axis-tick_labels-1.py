# Create a 2D chart with custom tick locations and labels on the y-axis.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.y_axis.tick_locations = (0.2, 0.4, 0.6, 1, 1.5, 2, 3)
chart.y_axis.tick_labels = [
    'Very small',
    'Small',
    'Still small',
    'Small?',
    'Not large',
    'Large?',
    'Very large',
]
chart.show()
#
#    Revert back to automatic tick placement.
#
chart.y_axis.tick_locations = None
chart.y_axis.tick_labels = None
chart.show()
#
#    Specify a custom label format to use (fixed notation with precision 2).
#
chart.y_axis.tick_labels = '2f'
chart.show()
