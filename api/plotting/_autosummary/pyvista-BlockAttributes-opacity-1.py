# Change the opacity of the second block of the dataset.
#
# Note how the zero index is the entire multiblock, so we have to add 1
# to our indexing to access the right block.
#
import pyvista as pv
dataset = pv.MultiBlock([pv.Cube(), pv.Sphere(center=(0, 0, 1))])
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset)
mapper.block_attr[2].opacity = 0.5
pl.show()
