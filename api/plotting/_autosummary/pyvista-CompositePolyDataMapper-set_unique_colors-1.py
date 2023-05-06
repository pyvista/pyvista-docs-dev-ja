# Set each block of the composite dataset to a unique color.
#
import pyvista as pv
dataset = pv.MultiBlock(
    [pv.Cube(), pv.Sphere(center=(0, 0, 1))]
)
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset)
mapper.set_unique_colors()
mapper.block_attr[1].color
# Expected:
## Color(name='tab:orange', hex='#ff7f0eff', opacity=255)
mapper.block_attr[2].color
# Expected:
## Color(name='tab:green', hex='#2ca02cff', opacity=255)
