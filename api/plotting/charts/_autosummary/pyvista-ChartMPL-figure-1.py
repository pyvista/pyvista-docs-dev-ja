# Create a matplotlib chart from an existing figure.
#
# .. pyvista-plot::
#
import pyvista as pv
import matplotlib.pyplot as plt
f, ax = plt.subplots()
_ = ax.plot([0, 1, 2], [2, 1, 3])
chart = pv.ChartMPL(f)
chart.figure is f
# Expected:
## True
chart.show()
