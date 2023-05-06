# Create a matplotlib chart from an existing figure.
#
# .. pyvista-plot::
#
import pyvista
import matplotlib.pyplot as plt
f, ax = plt.subplots()
_ = ax.plot([0, 1, 2], [2, 1, 3])
chart = pyvista.ChartMPL(f)
chart.figure is f
# Expected:
## True
chart.show()
