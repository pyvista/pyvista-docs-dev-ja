# Plot a random field of vectors and save a screenshot of it.
#
import numpy as np
import pyvista as pv
rng = np.random.default_rng(seed=0)
cent = rng.random((10, 3))
direction = rng.random((10, 3))
plotter = pv.Plotter()
_ = plotter.add_arrows(cent, direction, mag=2)
plotter.show()
