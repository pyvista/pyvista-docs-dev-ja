# Create a simple four value lookup table ranging from black to red.
#
import pyvista as pv
lut = pv.LookupTable()
lut.values = [
    [0, 0, 0, 255],
    [85, 0, 0, 255],
    [170, 0, 0, 255],
    [255, 0, 0, 255],
]
lut.values
# Expected:
## lookup_table_ndarray([[  0,   0,   0, 255],
##                       [ 85,   0,   0, 255],
##                       [170,   0,   0, 255],
##                       [255,   0,   0, 255]], dtype=uint8)
lut.plot()
