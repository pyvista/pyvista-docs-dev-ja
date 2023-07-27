import pyvista as pv
mesh = pv.Sphere()
mesh.get_cell(0).points
# Expected:
## array([[0.05405951, 0.        , 0.49706897],
##        [0.05287818, 0.0112396 , 0.49706897],
##        [0.        , 0.        , 0.5       ]])
