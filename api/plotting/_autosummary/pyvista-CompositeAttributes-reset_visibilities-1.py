# Hide the first block of a composite dataset and then show all by
# resetting visibilities.
#
# Note how the zero index is the entire multiblock, so we have to add 1
# to our indexing to access the right block.
#
import pyvista as pv
dataset = pv.MultiBlock(
    [pv.Cube(), pv.Sphere(center=(0, 0, 1))]
)
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset)
mapper.block_attr[1].visible = False
mapper.block_attr.reset_visibilities()
pl.show()
