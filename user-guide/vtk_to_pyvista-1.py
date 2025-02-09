import pyvista as pv
pv.set_plot_theme('document')
pv.set_jupyter_backend('static')
import numpy as np
xi = np.arange(300)
x, y = np.meshgrid(xi, xi)
values = 127.5 + (1.0 + np.sin(x/25.0)*np.cos(y/25.0))
grid = pv.ImageData(dimensions=(300, 300, 1))
grid.point_data["values"] = values.flatten(order="F")
grid.plot(cpos='xy', show_scalar_bar=False, cmap='coolwarm')