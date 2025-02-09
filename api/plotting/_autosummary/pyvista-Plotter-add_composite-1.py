# Add a sphere and a cube as a multiblock dataset to a plotter and then
# change the visibility and color of the blocks.
#
# Note index ``1`` and ``2`` are used to access the individual blocks of
# the composite dataset. This is because the :class:`pyvista.MultiBlock`
# is the root node of the "tree" and is index ``0``. This allows you to
# access individual blocks or the entire composite dataset itself in the
# case of multiple nested composite datasets.
#
import pyvista as pv
dataset = pv.MultiBlock([pv.Cube(), pv.Sphere(center=(0, 0, 1))])
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset)
mapper.block_attr[1].color = 'b'
mapper.block_attr[1].opacity = 0.5
mapper.block_attr[2].color = 'r'
pl.show()
