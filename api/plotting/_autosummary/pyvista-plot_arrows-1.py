# Plot a single random arrow.
#
import numpy as np
import pyvista as pv
rng = np.random.default_rng(seed=0)
cent = rng.random(3)
direction = rng.random(3)
pv.plot_arrows(cent, direction)
#
# Plot 100 random arrows.
#
import numpy as np
import pyvista as pv
cent = rng.random((100, 3))
direction = rng.random((100, 3))
pv.plot_arrows(cent, direction)
