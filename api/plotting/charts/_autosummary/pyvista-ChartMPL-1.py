# Plot streamlines of a vector field with varying colors (based on `this example <https://matplotlib.org/stable/gallery/images_contours_and_fields/plot_streamplot.html>`_).
#
# .. pyvista-plot::
#
import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
#
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)
#
f, ax = plt.subplots()
strm = ax.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
_ = f.colorbar(strm.lines)
_ = ax.set_title('Streamplot with varying Color')
plt.tight_layout()
#
chart = pv.ChartMPL(f)
chart.show()
