import pyvista as pv
mesh = pv.Sphere()
mesh.get_cell(0).center
# Expected:
## (0.03564589594801267, 0.0037465346977114677, 0.49804598093032837)
