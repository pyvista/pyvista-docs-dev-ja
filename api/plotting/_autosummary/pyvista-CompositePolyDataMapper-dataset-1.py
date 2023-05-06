import pyvista as pv
dataset = pv.MultiBlock(
    [pv.Cube(), pv.Sphere(center=(0, 0, 1))]
)
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset)
mapper.dataset  # doctest:+SKIP
# Expected:
## MultiBlock (...)
##   N Blocks:     2
##   X Bounds:     -0.500, 0.500
##   Y Bounds:     -0.500, 0.500
##   Z Bounds:     -0.500, 1.500
