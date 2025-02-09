import pyvista as pv
from pyvista import examples
filename = examples.download_caffeine(load=False)
filename.split('/')[-1]  # omit the path
# Expected:
## 'caffeine.pdb'
