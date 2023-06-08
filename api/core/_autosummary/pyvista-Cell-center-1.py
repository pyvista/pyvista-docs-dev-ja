import pyvista as pv
mesh = pv.Sphere()
mesh.get_cell(0).center
# Expected:
## (-0.0356, 0.00375, -0.498)
