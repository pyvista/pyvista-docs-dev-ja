# Make the cube of a multiblock dataset pickable and the sphere
# unpickable, then reset it.
#
# Note how the zero index is the entire multiblock, so we have to add 1
# to our indexing to access the right block.
#
import pyvista as pv
dataset = pv.MultiBlock([pv.Cube(), pv.Sphere(center=(0, 0, 1))])
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset)
mapper.block_attr[1].pickable = True
mapper.block_attr[2].pickable = False
mapper.block_attr.reset_pickabilities()
[
    mapper.block_attr[1].pickable,
    mapper.block_attr[2].pickable,
]
# Expected:
## [None, None]
pl.close()
