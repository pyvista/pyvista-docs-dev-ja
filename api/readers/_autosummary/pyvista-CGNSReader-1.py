# Load a CGNS file.  All arrays are loaded by default.
#
import pyvista
from pyvista import examples
filename = examples.download_cgns_multi(load=False)
reader = pyvista.CGNSReader(filename)
reader.load_boundary_patch = False
ds = reader.read()
ds[0][0].cell_data
# Expected:
## pyvista DataSetAttributes
## Association     : CELL
## Active Scalars  : None
## Active Vectors  : Momentum
## Active Texture  : None
## Active Normals  : None
## Contains arrays :
##     Density                 float64    (2928,)
##     Momentum                float64    (2928, 3)            VECTORS
##     EnergyStagnationDensity float64    (2928,)
##     ViscosityEddy           float64    (2928,)
##     TurbulentDistance       float64    (2928,)
##     TurbulentSANuTilde      float64    (2928,)
