# Add a sphere and a cube as a multiblock dataset to a plotter and then
# change the visibility and color of the blocks.
#
import pyvista as pv
dataset = pv.MultiBlock(
    [pv.Cube(), pv.Sphere(center=(0, 0, 1))]
)
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset)
mapper.block_attr[1].color = 'b'
mapper.block_attr[1].opacity = 0.1
mapper.block_attr[1]
# Expected:
## Composite Block Addr=... Attributes
## Visible:   None
## Opacity:   0.1
## Color:     Color(name='blue', hex='#0000ffff', opacity=255)
## Pickable   None
