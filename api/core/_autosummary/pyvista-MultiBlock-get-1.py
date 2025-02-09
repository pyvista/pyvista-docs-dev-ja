import pyvista as pv
from pyvista import examples
data = {'poly': pv.PolyData(), 'img': pv.ImageData()}
blocks = pv.MultiBlock(data)
blocks.get('poly')
# Expected:
## PolyData ...
blocks.get('cone')
