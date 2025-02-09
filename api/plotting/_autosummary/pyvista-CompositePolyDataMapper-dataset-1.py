import pyvista as pv
dataset = pv.MultiBlock([pv.Cube(), pv.Sphere(center=(0, 0, 1))])
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset)
mapper.dataset
# Expected:
## MultiBlock (...)
##   N Blocks:   2
##   X Bounds:   -5.000e-01, 5.000e-01
##   Y Bounds:   -5.000e-01, 5.000e-01
##   Z Bounds:   -5.000e-01, 1.500e+00
