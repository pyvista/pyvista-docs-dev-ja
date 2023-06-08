# Get the 0-th cell from a :class:`pyvista.PolyData`.
#
import pyvista as pv
mesh = pv.Sphere()
cell = mesh.get_cell(0)
cell  # doctest: +SKIP
# Expected:
## Cell (0x7fa760075a10)
##   Type:       <CellType.TRIANGLE: 5>
##   Linear:     True
##   Dimension:  2
##   N Points:   3
##   N Faces:    0
##   N Edges:    3
##   X Bounds:   -5.406e-02, -5.551e-17
##   Y Bounds:   0.000e+00, 1.124e-02
##   Z Bounds:   -5.000e-01, -4.971e-01
#
# Get the 0-th cell from a :class:`pyvista.UnstructuredGrid`.
#
from pyvista import examples
mesh = examples.load_hexbeam()
cell = mesh.get_cell(0)
cell  # doctest: +SKIP
# Expected:
## Cell (0x7fdc71a3c210)
##   Type:       <CellType.HEXAHEDRON: 12>
##   Linear:     True
##   Dimension:  3
##   N Points:   8
##   N Faces:    6
##   N Edges:    12
##   X Bounds:   0.000e+00, 5.000e-01
##   Y Bounds:   0.000e+00, 5.000e-01
##   Z Bounds:   0.000e+00, 5.000e-01
