import pyvista as pv
from pyvista import examples
#
filename = examples.download_m4_total_density(load=False)
filename.split('/')[-1]  # omit the path
# Expected:
## 'm4_TotalDensity.cube'
