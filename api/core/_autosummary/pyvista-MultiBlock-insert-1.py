# Insert a new :class:`pyvista.PolyData` at the start of the multiblock.
#
import pyvista as pv
data = {
    "cube": pv.Cube(),
    "sphere": pv.Sphere(center=(2, 2, 0)),
}
blocks = pv.MultiBlock(data)
blocks.keys()
# Expected:
## ['cube', 'sphere']
blocks.insert(0, pv.Plane(), "plane")
blocks.keys()
# Expected:
## ['plane', 'cube', 'sphere']
