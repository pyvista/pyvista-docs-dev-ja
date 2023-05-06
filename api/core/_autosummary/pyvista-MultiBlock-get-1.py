import pyvista as pv
from pyvista import examples
data = {"poly": pv.PolyData(), "uni": pv.UniformGrid()}
blocks = pv.MultiBlock(data)
blocks.get("poly")
# Expected:
## PolyData ...
blocks.get("cone")
