import pyvista as pv
from pyvista import examples
filename = examples.download_parched_canal_4k(load=False)
filename.split('/')[-1]  # omit the path
# Expected:
## 'parched_canal_4k.hdr'
reader = pv.get_reader(filename)
mesh = reader.read()
mesh
# Expected:
## ImageData (...)
##   N Cells:      8382465
##   N Points:     8388608
##   X Bounds:     0.000e+00, 4.095e+03
##   Y Bounds:     0.000e+00, 2.047e+03
##   Z Bounds:     0.000e+00, 0.000e+00
##   Dimensions:   4096, 2048, 1
##   Spacing:      1.000e+00, 1.000e+00, 1.000e+00
##   N Arrays:     1
