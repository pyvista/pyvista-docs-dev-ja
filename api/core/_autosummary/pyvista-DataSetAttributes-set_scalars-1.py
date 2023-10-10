import pyvista as pv
mesh = pv.Cube()
mesh.clear_data()
scalars = range(mesh.n_points)
mesh.point_data.set_scalars(scalars, 'my-scalars')
mesh.point_data
# Expected:
## pyvista DataSetAttributes
## Association     : POINT
## Active Scalars  : my-scalars
## Active Vectors  : None
## Active Texture  : None
## Active Normals  : None
## Contains arrays :
##     my-scalars              int64      (8,)                 SCALARS
