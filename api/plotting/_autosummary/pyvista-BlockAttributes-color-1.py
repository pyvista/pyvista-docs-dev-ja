# Set the colors of a composite dataset to red and blue.
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
mapper.block_attr[1].color = 'r'
mapper.block_attr[2].color = 'b'
pl.show()
