# Pop the ``"cube"`` multiblock.
#
import pyvista as pv
data = {
    'cube': pv.Cube(),
    'sphere': pv.Sphere(center=(2, 2, 0)),
}
blocks = pv.MultiBlock(data)
blocks.keys()
# Expected:
## ['cube', 'sphere']
cube = blocks.pop('cube')
blocks.keys()
# Expected:
## ['sphere']
