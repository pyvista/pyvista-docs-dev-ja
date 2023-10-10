# Plot a simple sine wave as a scatter and line plot.
#
import pyvista as pv
import numpy as np
x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x)
chart = pv.Chart2D()
_ = chart.scatter(x, y)
_ = chart.line(x, y, 'r')
chart.show()
#
# Combine multiple types of plots in the same chart.
#
rng = np.random.default_rng(1)
x = np.arange(1, 8)
y = rng.integers(5, 15, 7)
e = np.abs(rng.normal(scale=2, size=7))
z = rng.integers(0, 5, 7)
chart = pv.Chart2D()
_ = chart.area(x, y-e, y+e, color=(0.12, 0.46, 0.71, 0.2))
_ = chart.line(x, y, color="tab:blue", style="--", label="Scores")
_ = chart.scatter(x, y, color="tab:blue", style="d")
_ = chart.bar(x, z, color="tab:orange", label="Violations")
chart.x_axis.tick_locations = x
chart.x_axis.tick_labels = ["Mon", "Tue", "Wed", "Thu", "Fri",
                            "Sat", "Sun"]
chart.x_label = "Day of week"
chart.show()
