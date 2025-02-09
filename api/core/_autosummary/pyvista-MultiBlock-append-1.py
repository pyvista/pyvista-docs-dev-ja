import pyvista as pv
from pyvista import examples
data = {
    'cube': pv.Cube(),
    'sphere': pv.Sphere(center=(2, 2, 0)),
}
blocks = pv.MultiBlock(data)
blocks.append(pv.Cone())
len(blocks)
# Expected:
## 3
blocks.append(examples.load_uniform(), 'uniform')
blocks.keys()
# Expected:
## ['cube', 'sphere', 'Block-02', 'uniform']
