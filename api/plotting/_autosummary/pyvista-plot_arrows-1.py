# Plot a single random arrow.
#
import numpy as np
import pyvista as pv
cent = np.random.random(3)
direction = np.random.random(3)
pv.plot_arrows(cent, direction)
#
# Plot 100 random arrows.
#
import numpy as np
import pyvista as pv
cent = np.random.random((100, 3))
direction = np.random.random((100, 3))
pv.plot_arrows(cent, direction)
