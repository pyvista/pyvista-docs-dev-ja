import pyvista as pv
from pyvista import examples
data = {
    'cube': pv.Cube(),
    'sphere': pv.Sphere(center=(2, 2, 0)),
}
blocks = pv.MultiBlock(data)
blocks_uniform = pv.MultiBlock({'uniform': examples.load_uniform()})
blocks.extend(blocks_uniform)
len(blocks)
# Expected:
## 3
blocks.keys()
# Expected:
## ['cube', 'sphere', 'uniform']
