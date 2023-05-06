from pyvista import examples
mesh = examples.load_uniform()
points = mesh.cast_to_poly_points(pass_cell_data=True)
type(points)
# Expected:
## <class 'pyvista.core.pointset.PolyData'>
points.n_arrays
# Expected:
## 2
points.point_data
# Expected:
## pyvista DataSetAttributes
## Association     : POINT
## Active Scalars  : Spatial Point Data
## Active Vectors  : None
## Active Texture  : None
## Active Normals  : None
## Contains arrays :
##     Spatial Point Data      float64    (1000,)              SCALARS
points.cell_data
# Expected:
## pyvista DataSetAttributes
## Association     : CELL
## Active Scalars  : None
## Active Vectors  : None
## Active Texture  : None
## Active Normals  : None
## Contains arrays :
##     Spatial Cell Data       float64    (1000,)
