import pyvista as pv
import numpy as np
data = {
    "cube": pv.Cube(),
    "sphere": pv.Sphere(center=(2, 2, 0)),
}
blocks = pv.MultiBlock(data)
blocks.replace(1, pv.Sphere(center=(10, 10, 10)))
blocks.keys()
# Expected:
## ['cube', 'sphere']
np.allclose(blocks[1].center, [10.0, 10.0, 10.0])
# Expected:
## True
