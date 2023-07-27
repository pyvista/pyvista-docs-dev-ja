# First, compute cell normals.
#
import pyvista
mesh = pyvista.Plane(i_resolution=1, j_resolution=1)
mesh.point_data
# Expected:
## pyvista DataSetAttributes
## Association     : POINT
## Active Scalars  : None
## Active Vectors  : None
## Active Texture  : TextureCoordinates
## Active Normals  : Normals
## Contains arrays :
##     Normals                 float32    (4, 3)               NORMALS
##     TextureCoordinates      float32    (4, 2)               TCOORDS
#
mesh.point_data.active_normals
# Expected:
## pyvista_ndarray([[0., 0., 1.],
##                  [0., 0., 1.],
##                  [0., 0., 1.],
##                  [0., 0., 1.]], dtype=float32)
#
# Assign normals to the cell arrays.  An array will be added
# named ``"Normals"``.
#
mesh.cell_data.active_normals = [[0.0, 0.0, 1.0]]
mesh.cell_data
# Expected:
## pyvista DataSetAttributes
## Association     : CELL
## Active Scalars  : None
## Active Vectors  : None
## Active Texture  : None
## Active Normals  : Normals
## Contains arrays :
##     Normals                 float64    (1, 3)               NORMALS
