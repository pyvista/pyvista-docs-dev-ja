# Create a matplotlib chart with title 'My Chart'.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
import matplotlib.pyplot as plt
f, ax = plt.subplots()
_ = ax.plot([0, 1, 2], [2, 1, 3])
chart = pv.ChartMPL(f)
chart.title = 'My Chart'
chart.show()
