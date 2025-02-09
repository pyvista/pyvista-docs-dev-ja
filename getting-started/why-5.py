import pyvista
import numpy as np

# Make a grid
x, y, z = np.meshgrid(np.linspace(-5, 5, 20),
                      np.linspace(-5, 5, 20),
                      np.linspace(-5, 5, 5),
                      indexing='ij')

points = np.empty((x.size, 3))
points[:, 0] = x.ravel('F')
points[:, 1] = y.ravel('F')
points[:, 2] = z.ravel('F')

# Compute a direction for the vector field
direction = np.sin(points)**3

# plot using the plotting class
pl = pyvista.Plotter()
pl.add_arrows(points, direction, 0.5)
pl.show()