import pyvista as pv
import numpy as np
arrays = np.random.default_rng().random((100, 3))
table = pv.Table(arrays)
