import pyvista as pv
import numpy as np
x = np.arange(12)
p_min = [11, 0, 16, 2, 23, 18, 25, 17, 9, 12, 14, 21]
p_max = [87, 64, 92, 73, 91, 94, 107, 101, 84, 88, 95, 103]
chart = pv.Chart2D()
_ = chart.area(x, p_min, p_max)
chart.x_axis.tick_locations = x
chart.x_axis.tick_labels = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec',
]
chart.x_axis.label = 'Month'
chart.y_axis.label = 'Precipitation [mm]'
chart.show()
