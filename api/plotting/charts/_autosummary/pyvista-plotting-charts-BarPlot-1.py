# Create a stacked bar chart showing the average time spent on activities
# throughout the week.
#
import pyvista as pv
import numpy as np
x = np.arange(1, 8)
y_s = [7, 8, 7.5, 8, 7.5, 9, 10]
y_h = [2, 3, 2, 2.5, 1.5, 4, 6.5]
y_w = [8, 8, 7, 8, 7, 0, 0]
y_r = [5, 2.5, 4.5, 3.5, 6, 9, 6.5]
y_t = [2, 2.5, 3, 2, 2, 2, 1]
labels = ["Sleep", "Household", "Work", "Relax", "Transport"]
chart = pv.Chart2D()
_ = chart.bar(x, [y_s, y_h, y_w, y_r, y_t], label=labels)
chart.x_axis.tick_locations = x
chart.x_axis.tick_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
chart.x_label = "Day of week"
chart.y_label = "Average time spent"
chart.grid = False  # Disable the grid lines
chart.show()
