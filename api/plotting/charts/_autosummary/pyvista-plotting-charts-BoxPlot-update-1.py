# Create a box plot from a standard Gaussian dataset.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
import numpy as np
rng = np.random.default_rng(
    1
)  # Seeded random number generator for data generation
chart = pv.ChartBox([rng.normal(size=100)])
chart.show()
#
#    Update the box plot (shift the standard Gaussian distribution).
#
chart.plot.update([rng.normal(loc=2, size=100)])
chart.show()
