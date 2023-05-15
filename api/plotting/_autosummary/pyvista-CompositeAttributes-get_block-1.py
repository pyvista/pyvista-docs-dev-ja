# Add a composite dataset to a plotter and access its block attributes.
# Note how the zero index is the entire multiblock and you can use ``1``
# and ``2`` to access the individual sub-blocks.
#
import pyvista as pv
dataset = pv.MultiBlock(
    [pv.Cube(), pv.Sphere(center=(0, 0, 1))]
)
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset)
mapper.block_attr.get_block(0)
# Expected:
## MultiBlock (...)
##   N Blocks    2
##   X Bounds    -0.500, 0.500
##   Y Bounds    -0.500, 0.500
##   Z Bounds    -0.500, 1.500
#
# Note this is the same as using ``__getitem__``
#
mapper.block_attr[0]
# Expected:
## Composite Block Addr=... Attributes
## Visible:   None
## Opacity:   None
## Color:     None
## Pickable   None
