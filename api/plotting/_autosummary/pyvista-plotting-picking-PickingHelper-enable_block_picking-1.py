# Enable block picking with a multiblock dataset. Left clicking will turn
# blocks blue while right picking will turn the block back to the default
# color.
#
import pyvista as pv
multiblock = pv.MultiBlock(
    [pv.Cube(), pv.Sphere(center=(0, 0, 1))]
)
pl = pv.Plotter()
actor, mapper = pl.add_composite(multiblock)
def turn_blue(index, dataset):
    mapper.block_attr[index].color = 'blue'
pl.enable_block_picking(callback=turn_blue, side='left')
def clear_color(index, dataset):
    mapper.block_attr[index].color = None
pl.enable_block_picking(callback=clear_color, side='right')
pl.show()
