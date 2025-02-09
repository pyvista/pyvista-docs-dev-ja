# Make the cube of a multiblock dataset pickable and the sphere unpickable.
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
pl.close()
#
# See :ref:`composite_picking_example` for a full example using block
